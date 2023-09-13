# A user-friendly Python email toolkit

## Installation
```bash
python3 -m pip install mailkit
```

## Usage on CMD
```bash
Usage: python -m mailkit.bin.main [OPTIONS] COMMAND [ARGS]...

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

```

### *`mailkit config`*
```bash
Usage: python -m mailkit.bin.main config [OPTIONS]

  initialize the configuration file

Options:
  -s, --show      show the current configuration
  -?, -h, --help  Show this message and exit.


mailkit config
# flowing the instruction to complete the configuration
"
>>> SMTP host: smtp.exmail.qq.com
>>> SMTP port [465]: 
>>> SMTP username: suqingdong@novogene.com
>>> SMTP password: 
>>> SMTP use ssl [True]: 
>>> SMTP timeout [10]: 
login success.
Saved configuration to ~/.mailkit.env
"

# you can also use envernment variables
export SMTP_HOST=smtp.gmail.com
export SMTP_PORT=465
export SMTP_USERNAME=suqingdong@gmail.com
export SMTP_PASSWORD=YOUR_PASSWORD
export SMTP_USE_SSL=True
export SMTP_TIMEOUT=10
```

### *`mailkit send`*
```bash
Usage: python -m mailkit.bin.main send [OPTIONS]

  send email to user(s)

Options:
  -f, --from-addr TEXT     the display address of the sender, default is the login username
  -t, --to-addrs TEXT      the recipient address(es)  [required]
  -s, --subject TEXT       the subject of the email  [required]
  -b, --body TEXT          the body of the email
  -a, --attachments TEXT   the attachments of the email
  -C, --charset TEXT       the charset of the email  [default: utf-8]
  -c, --content-type TEXT  the content type of the email, eg.: plain, html [default: plain]
  -cc, --cc TEXT           the cc address(es)
  -bcc, --bcc TEXT         the bcc address(es)
  -h, -?, --help           Show this message and exit.


# Examples:

# basic usage
mailkit send -t "to@example.com" -s "subject" -b "body"

# use charset
mailkit send -t "to@example.com" -s "subject" -b "body" -C "gbk"

# use content-type
mailkit send -t "to@example.com" -s "subject" -b "<h1>body</h1>" -C "utf-8" -c "html"

# use cc and bcc
mailkit send -t "to@example.com" -s "subject" -b "body" -cc "cc@example.com" -bcc "bcc@example.com"

# use attachments
mailkit send -t "to@example.com" -s "subject" -b "body" -a "attachment.txt"

# multiple parameters
mailkit send -t "to_1@example.com" -t "to_2@example.com" -s "subject" -b "body" -a "attachment.txt" -a "attachment_2.txt"

# auth with parameters
mailkit -H smtp.gmail.com -u username@gmail.com -p password send -t "to@example.com" -s "subject" -b "body"

# auth with an env_file
mailkit -e .env send -t "to@example.com" -s "subject" -b "body"
```

## Usage in Python
```python
from mailkit.core import SendEmail

mail = SendEmail()

# basic usage
mail.send('to@example.com', 'subject', 'body')

# use content-type
mail.send('to@example.com', 'subject', '<h1>body</h1>', content_type='html')

# use attachments
mail.send('to@example.com', 'subject', 'body', attachments=['attachment.txt'])

# close the connection
mail.close()

# use with mode
with SendEmail() as mail:
    mail.send('to@example.com', 'subject', 'body')
```
### `mailkit.core.SendEmail`
```python
class SendEmail(mailkit.core.smtp.config.SmtpConfig)
 |  SendEmail(_case_sensitive: 'bool | None' = None,_env_prefix: 'str | None' = None, _env_file: 'DotenvType | None' = PosixPath('.'), _env_file_encoding: 'str | None' = None, _env_nested_delimiter: 'str | None' = None, _secrets_dir: 'str | Path | None' = None, *, host: str, port: Union[int, NoneType] = None, username: str, password: str, use_ssl: bool = True, use_tls: bool = False, timeout: int = 10) -> None
 |  
 |  send(from_addr: str, to_addrs: Union[str, List[str]], subject: str, body: str = '', content_type: str = 'plain', charset: str = 'utf-8', cc: Union[str, List[str]] = '', bcc: Union[str, List[str]] = '', attachments: Union[str, List[str], NoneType] = None) -> None
 |  
 |  close(self)
 |  
 |  login(self)
 |  
 |  model_dump(self, *, mode: "Literal[('json', 'python')] | str" = 'python', include: 'IncEx' = None, exclude: 'IncEx' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: 'bool' = True) -> 'dict[str, Any]'

```
