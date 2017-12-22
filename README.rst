qu
==

.. image:: https://img.shields.io/pypi/l/qu.svg
    :target: https://pypi.python.org/pypi/qu

.. image:: https://img.shields.io/pypi/v/qu.svg
    :target: https://pypi.python.org/pypi/qu

.. image:: https://img.shields.io/pypi/pyversions/qu.svg
    :target: https://pypi.python.org/pypi/qu

.. image:: https://travis-ci.org/cls1991/qu.svg?branch=master
    :target: https://travis-ci.org/cls1991/qu

Quickly generating unique url of a picture for markdown files.

.. image:: https://asciinema.org/a/41WfW5ehC7RRXQ8WA4unZG5WY.png
    :target: https://asciinema.org/a/41WfW5ehC7RRXQ8WA4unZG5WY

☤ Quickstart
------------

Upload an image file to qiniu:

::

    $ qu /somewhere/1.png 2.png
    $ qu /somewhere/1.png

Set configuration of qiniu:

::

    $ qu wc --access_key=AK --secret_key=SK --bucket_name=BN --domain_name=DN

List local configuration of qiniu:

::

    $ qu sc
    $ qu sc --format-type json

☤ Installation
--------------

You can install "qu" via pip from `PyPI <https://pypi.python.org/pypi/qu>`_:

::

    $ pip install qu
	
☤ Usage
-------

::

    $ qu --help
    Usage: qu [OPTIONS] COMMAND [ARGS]...

      Quickly generating unique url of a picture for markdown files.

    Options:
      --help  Show this message and exit.

    Commands:
      dc      Clear configuration of qiniu.
      sc      Show configuration of qiniu.
      upload  Upload an image to qiniu.
      wc      Set configuration of qiniu.


    $ qu wc --help
    Usage: qu wc [OPTIONS]

      Set configuration of qiniu.

    Options:
      -ak, --access_key TEXT   qiniu access_key.
      -sk, --secret_key TEXT   qiniu secret_key.
      -bn, --bucket_name TEXT  qiniu bucket_name.
      -dm, --domain_name TEXT  qiniu domain_name.
      --help                   Show this message and exit.


    $ qu sc --help
    Usage: qu sc [OPTIONS]

      Show configuration of qiniu.

    Options:
      --format-type [json|xml]  output format type.
      --help                    Show this message and exit.
