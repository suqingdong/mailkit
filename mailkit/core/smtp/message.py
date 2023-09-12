import os
from typing import List, Optional, Union
from dataclasses import dataclass

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


@dataclass
class MessageField:
    """
    Fields:
    """
    from_addr: str
    to_addrs: Union[str, List[str]]
    subject: str
    body: str = ''
    content_type: str = 'plain'
    charset: str = 'utf-8'
    cc: Union[str, List[str]] = ''
    bcc: Union[str, List[str]] = ''
    attachments: Optional[Union[str, List[str]]] = None


class Message(MessageField):

    _message = None

    @property
    def message(self):
        """Property to access the MIME multipart message object."""
        if self._message is None:
            self._message = MIMEMultipart()
            self.create_message()
        return self._message

    def create_message(self):
        """Create and populate the MIME multipart message object."""
        self._set_headers()
        if self.body:
            self._attach_body()
        if self.attachments:
            self._attach_attachments()

    @staticmethod
    def _deal_addrs(addrs: Union[str, List[str]]):
        """
        Deal with the email addresses.
        """
        if not isinstance(addrs, str):
            return ','.join(addrs)
        return addrs

    def _set_headers(self):
        """Set the headers for the email message."""
        self.message['From'] = self.from_addr
        self.message['To'] = self._deal_addrs(self.to_addrs)
        if self.cc:
            self.message['Cc'] = self._deal_addrs(self.cc)
        if self.bcc:
            self.message['Bcc'] = self._deal_addrs(self.bcc)
        self.message['Subject'] = Header(self.subject, self.charset)

    def _attach_body(self):
        """Attach the body to the email message."""
        if self.body and os.path.isfile(self.body):
            with open(self.body) as f:
                body = f.read()
        else:
            body = self.body
        msg = MIMEText(body, _subtype=self.content_type, _charset=self.charset)
        self.message.attach(msg)

    def _attach_attachments(self):
        """Attach files to the email message."""
        if isinstance(self.attachments, str):
            attachments = self.attachments.split(',')
        else:
            attachments = self.attachments
        for file in attachments:
            if os.path.isfile(file):
                with open(file, 'rb') as f:
                    part = MIMEApplication(f.read())
                    part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
                    self.message.attach(part)


if __name__ == '__main__':
    Message(from_addr='suqingdong', to_addrs='suqingdong@novogene.com', subject='test')
