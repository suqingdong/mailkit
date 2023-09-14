Usage on CMD
=============

.. code-block:: bash

    Usage: mailkt [OPTIONS] COMMAND [ARGS]...

    A user-friendly Python email toolkit

    Options:
      --version              Show the version and exit.
      -H, --host TEXT        SMTP server hostname or IP address
      -P, --port INTEGER     SMTP server port
      -u, --username TEXT    SMTP server username
      -p, --password TEXT    SMTP server password
      -s, --use-ssl BOOLEAN  Use SSL connection  [default: True]
      -t, --timeout INTEGER  SMTP server timeout  [default: 10]
      -e, --env-file TEXT    The environment file to load  [default: ~/.mailkit.env]
      -h, -?, --help         Show this message and exit.

    Commands:
      config  initialize the configuration file
      send    send email to user(s)


`mailkit send`
---------------

.. code-block:: bash

    Usage: mailkt send [OPTIONS]

        send email to user(s)

    Options:
    -f, --from-addr TEXT     the display address of the sender, default is the login username
    -t, --to-addrs TEXT      the recipient address(es)  [required]
    -s, --subject TEXT       the subject of the email  [required]
    -b, --body TEXT          the body of the email
    -a, --attachments TEXT   the attachments of the email
    -C, --charset TEXT       the charset of the email  [default: utf-8]
    -c, --content-type TEXT  the content type of the email, e.g.: plain, html [default: plain]
    -cc, --cc TEXT           the cc address(es)
    -bcc, --bcc TEXT         the bcc address(es)
    -h, -?, --help           Show this message and exit.

Examples:

.. code-block:: bash

    # Basic usage
    mailkit send -t "to@example.com" -s "subject" -b "body"

    # Use charset
    mailkit send -t "to@example.com" -s "subject" -b "body" -C "gbk"

    # Use content-type
    mailkit send -t "to@example.com" -s "subject" -b "<h1>body</h1>" -C "utf-8" -c "html"

    # Use cc and bcc
    mailkit send -t "to@example.com" -s "subject" -b "body" -cc "cc@example.com" -bcc "bcc@example.com"

    # Use attachments
    mailkit send -t "to@example.com" -s "subject" -b "body" -a "attachment.txt"

    # Multiple parameters
    mailkit send -t "to_1@example.com" -t "to_2@example.com" -s "subject" -b "body" -a "attachment.txt" -a "attachment_2.txt"

    # Auth with parameters
    mailkit -H smtp.gmail.com -u username@gmail.com -p password send -t "to@example.com" -s "subject" -b "body"

    # Auth with an env_file
    mailkit -e .env send -t "to@example.com" -s "subject" -b "body"


