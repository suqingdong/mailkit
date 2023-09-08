class MailKitError(Exception):
    """Base exception class for MailKit"""
    pass


class LoginError(MailKitError):
    """Exception raised for login-related errors."""

    def __init__(self, message="Failed to login to SMTP server", *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class SendMailError(MailKitError):
    """Exception raised for errors while sending mail."""

    def __init__(self, message="Failed to send email", *args, **kwargs):
        super().__init__(message, *args, **kwargs)
