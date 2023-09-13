============
Configuration
============

.. code-block:: bash

    Usage: python -m mailkit.bin.main config [OPTIONS]

    initialize the configuration file

    Options:
    -s, --show      show the current configuration
    -?, -h, --help  Show this message and exit.

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

    # You can also use environment variables
    export SMTP_HOST=smtp.gmail.com
    export SMTP_PORT=465
    export SMTP_USERNAME=suqingdong@gmail.com
    export SMTP_PASSWORD=YOUR_PASSWORD
    export SMTP_USE_SSL=True
    export SMTP_TIMEOUT=10
