import smtplib
import functools
from inspect import signature
import click

from mailkit.error import LoginError, SendMailError
from .message import Message
from .config import SmtpConfig


message_signature = signature(Message)

def wrap_message_signature(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.__signature__ = message_signature
    return wrapper


class SendEmail(SmtpConfig):
    _smtp = None

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.smtp is not None:
            self.smtp.quit()

    @property
    def smtp(self):
        if self._smtp is None:
            self.login()
        return self._smtp

    def login(self):
        SmtpType = smtplib.SMTP_SSL if self.use_ssl else smtplib.SMTP
        port = self.port or smtplib.SMTP_SSL_PORT if self.use_ssl else smtplib.SMTP_PORT
        try:
            self._smtp = SmtpType(self.host, port, timeout=self.timeout)
            self._smtp.login(self.username, self.password)
            click.secho('login success.', fg='green', err=True)
        except Exception as e:
            raise LoginError(click.style(f'login failed as: {e}', fg='red'))

    @wrap_message_signature
    def send(self, **kwargs):
        kwargs['from_addr'] = kwargs.get('from_addr', self.username)
        msg = Message(**kwargs).message
        try:
            self.smtp.sendmail(self.username, kwargs['to_addrs'], msg.as_string())
            click.secho('email has send to: {to_addrs}'.format(**kwargs), fg='green', err=True)
        except Exception as e:
            raise SendMailError(f'send email failed as: {e}')
