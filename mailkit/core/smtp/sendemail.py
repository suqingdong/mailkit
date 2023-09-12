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
    # def __init__(self, host, username, password, port=None, use_ssl=True, timeout=10):
    #     self.host = host
    #     self.port = port or smtplib.SMTP_SSL_PORT if use_ssl else smtplib.SMTP_PORT
    #     self.username = username
    #     self.password = password
    #     self.use_ssl = use_ssl
    #     self.timeout = timeout

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


if __name__ == '__main__':
    from mailkit.config import SMTP_Config

    settings = SMTP_Config(env_file='.env')
    print(settings.model_dump())
    sender = SendEmail(**settings.model_dump())
    sender.send(to_addrs='suqingdong@novogene.com', subject='测试plain', body='测试')
    sender.send(to_addrs='suqingdong@novogene.com', subject='测试html', body='<h1>你好!</h1>', content_type='html')
