QuickStart
==========

1 Installation

.. code-block:: bash

    python3 -m pip install mailkit

2 Configuration

.. code-block:: bash

    mailkit config

    mailkit config --show


3.1 SendEmail on Command

.. code-block:: bash

    mailkit send --help

    mailkit send -t to@email.com -s subject -b body

    mailkit send -t to_1@email.com -t to_2@email.com -s subject -b '<h1>hello world</h1>' -c html -a result.zip


3.2 SendEmail in Python

.. code-block:: python

    from mailkit import SendEmail

    with SendEmail() as mail:
        mail.send(to='to@email.com', subject='subject', body='body')
