# coding: utf8


import os
import subprocess


def execute(cmd):
    out = None
    if cmd:
        try:
            out, err = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()
        except ValueError:
            pass

    return out


def test_qu():
    assert execute(['qu'])


def test_qu_wc():
    access_key = os.environ['access_key']
    secret_key = os.environ['secret_key']
    bucket_name = os.environ['bucket_name']
    domain_name = os.environ['domain_name']
    assert execute(['qu', 'wc', '--access_key', access_key, '--secret_key', secret_key, '--bucket_name', bucket_name,
                    '--domain_name', domain_name])


def test_qu_sc():
    assert execute(['qu', 'sc'])
    assert execute(['qu', 'sc', '--format_type', 'json'])


def test_qu_dc():
    assert execute(['qu', 'dc'])


def test_qu_help():
    assert execute(['qu', '--help'])
    assert execute(['qu', 'wc', '--help'])
    assert execute(['qu', 'sc', '--help'])
