# coding: utf8

"""
    quick-url: Simply upload image, then return an unique url.
               Currently only qiniu is supported.
"""

try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser
import json
import os
import sys

import click
from qiniu import (
    Auth, etag, put_file
)

_ver = sys.version_info

# Python 2.x?
is_py2 = (_ver[0] == 2)

# Python 3.x?
is_py3 = (_ver[0] == 3)

HERE = os.path.abspath(os.path.dirname(__file__))
CONFIG_DIR = 'config'
CONFIG_CFG = '.config.cfg'
SECTION = 'qn'
PROTOCOL = 'http'
VAlID_EXTENSIONS = ('.png', '.jpeg', '.jpg', '.gif')


def _write_cfg(data):
    """
    :param data:
    :return:
    """
    assert isinstance(data, dict)
    config = ConfigParser.ConfigParser()
    config.add_section(SECTION)

    for k, v in data.items():
        config.set(SECTION, k, v)

    parent = os.path.join(HERE, CONFIG_DIR)
    if not _check_exist(parent):
        os.mkdir(parent)
    with open(os.path.join(parent, CONFIG_CFG), 'w') as f:
        config.write(f)


def _read_cfg():
    """
    :return: 
    """
    config = ConfigParser.ConfigParser()
    config.read(os.path.join(HERE, CONFIG_DIR, CONFIG_CFG))

    cfg = dict()

    for cf in config.items(SECTION):
        cfg[cf[0]] = cf[1]

    return cfg


def _del_cfg():
    """
    :return:
    """
    path = os.path.join(HERE, CONFIG_DIR, CONFIG_CFG)
    if _check_exist(path):
        os.remove(path)


def _check_exist(file_path=None):
    """
    :param file_path:
    :return:
    """
    if not file_path:
        file_path = os.path.join(HERE, CONFIG_DIR, CONFIG_CFG)

    return os.path.exists(file_path)


def _check_extension(file_path):
    """
    :param file_path:
    :return:
    """
    ext = _get_extension(file_path)
    return ext.lower() in VAlID_EXTENSIONS


def _get_extension(file_path):
    """
    :param file_path:
    :return:
    """
    return os.path.splitext(file_path)[1]


def _get_name(file_path):
    """
    :param file_path:
    :return:
    """
    return os.path.basename(file_path)


def _upload(file_path, key=None):
    """
    :param file_path:
    :param key:
    :return:
    """
    cfg = _read_cfg()

    access_key = cfg.get('access_key')
    secret_key = cfg.get('secret_key')
    bucket_name = cfg.get('bucket_name')
    domain_name = cfg.get('domain_name')

    q = Auth(access_key, secret_key)
    if not key:
        key = _get_name(file_path)
    token = q.upload_token(bucket_name, _encode(key), 3600)
    ret, info = put_file(token, _encode(key), _encode(file_path))

    suc = ret['key'] == key and ret['hash'] == etag(file_path)

    return True, '{0}://{1}/{2}'.format(PROTOCOL, domain_name, _encode(key)) if suc else (False, info.error)


def _encode(u):
    """
    :param u:
    :return:
    """
    if is_py2 and isinstance(u, unicode):
        return u.encode('utf8')

    return u


def _format(data, format_type='json'):
    """
    :param data:
    :param format_type:
    :return:
    """
    if format_type == 'json':
        return json.dumps(data, indent=4)

    # @TODO: support other format types.
    return str(data)


@click.group()
def cli():
    """Quickly generating unique url of a picture for markdown files."""
    pass


@cli.command()
@click.option('-ak', '--access_key', help='qiniu access_key.')
@click.option('-sk', '--secret_key', help='qiniu secret_key.')
@click.option('-bn', '--bucket_name', help='qiniu bucket_name.')
@click.option('-dm', '--domain_name', help='qiniu domain_name.')
def wc(**kwargs):
    """Set configuration of qiniu."""
    for k in kwargs:
        if not kwargs[k]:
            click.echo('{0} cannot be empty!'.format(k))
            sys.exit(1)

    _write_cfg(kwargs)


@cli.command()
@click.option('--format-type', type=click.Choice(['json', 'xml']), default='json', help='output format type.')
def sc(format_type):
    """Show configuration of qiniu."""
    if not _check_exist():
        click.echo(
            click.style('{0} not exists, please run `qu wc` to set configuration first.'.format(CONFIG_CFG),
                        fg='yellow'))
        sys.exit(1)

    click.secho(click.style(_format(_read_cfg(), format_type), fg='green'))


@cli.command()
def dc():
    """Clear configuration of qiniu."""
    _del_cfg()
    click.secho(click.style('Clear completed.', fg='green'))


@cli.command()
@click.argument('file_path')
@click.argument('key', required=False)
def up(file_path, key):
    """Upload an image to qiniu."""
    if not _check_exist():
        click.echo(click.style('{0} not exists, please run `qu wc` to set configuration first.'.format(CONFIG_CFG),
                               fg='yellow'))
        sys.exit(1)

    if not _check_exist(file_path):
        click.secho(click.style('{0} is not found.'.format(_encode(file_path)), fg='yellow'))
        sys.exit(1)

    if not _check_extension(file_path):
        click.secho(click.style('{0} is not supported.'.format(_encode(file_path)), fg='yellow'))
        sys.exit(1)

    ok, msg = _upload(file_path, key)
    click.secho(click.style(msg, fg='blue' if ok else 'red'))


if __name__ == '__main__':
    cli()
