Usage in Python
===============

.. code-block:: python

    from mailkit.core import SendEmail

    # Default auth with ~/.mailkit.env
    mail = SendEmail()

    # Basic usage
    mail.send('to@example.com', 'subject', 'body')

    # Use content-type
    mail.send('to@example.com', 'subject', '<h1>body</h1>', content_type='html')

    # Use attachments
    mail.send('to@example.com', 'subject', 'body', attachments=['attachment.txt'])

    # Close the connection
    mail.close()

    # Use with mode
    with SendEmail() as mail:
        mail.send('to@example.com', 'subject', 'body')

.. code-block:: python

    # Auth with another env_file
    mail = SendEmail(_env_file='.env')

    # Auth with parameters
    mail = SendEmail(host='smtp.gmail.com', port=465, username='username@gmail.com', password='password')

    # Auth with environment variables
    import os
    os.environ['SMTP_HOST'] = 'smtp.gmail.com'
    os.environ['SMTP_PORT'] = 465
    os.environ['SMTP_USERNAME'] = 'username@gmail.com'
    os.environ['SMTP_PASSWORD'] = 'password'
    os.environ['SMTP_USE_SSL'] = True
    os.environ['SMTP_TIMEOUT'] = 10
    mail = SendEmail()
