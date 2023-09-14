==============
Configuration
==============

.. code-block:: bash

    Usage: mailkit config [OPTIONS]

    initialize the configuration file

    Options:
    -s, --show      show the current configuration
    -?, -h, --help  Show this message and exit.


`mailkit config`
================

.. code-block:: bash

    mailkit config
    # Follow the instructions to complete the configuration
    "
    >>> SMTP host: smtp.exmail.qq.com
    >>> SMTP port [465]:
    >>> SMTP username: suqingdong@novogene.com
    >>> SMTP password:
    >>> SMTP use ssl [True]:
    >>> SMTP timeout [10]:
    Login success.
    Saved configuration to ~/.mailkit.env
    "


use environment variables
=========================

.. code-block:: bash

    export SMTP_HOST=smtp.gmail.com
    export SMTP_PORT=465
    export SMTP_USERNAME=suqingdong@gmail.com
    export SMTP_PASSWORD=YOUR_PASSWORD
    export SMTP_USE_SSL=True
    export SMTP_TIMEOUT=10
