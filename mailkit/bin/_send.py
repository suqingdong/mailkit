import click
from pydantic import ValidationError

from mailkit.core.smtp import SendEmail
from mailkit.error import LoginError

from ._config import initialize_config


__epilog__ = click.style('''                
\n\b
examples:
  -t to@mail.com -s "test plain" -b "hello world"
  -t to@mail.com -s "test html" -b "<h1>hello world</h1>" -c html
  -t to@mail.com -s "test file as body" -b README.md
  -t to_1@mail.com -t to_2@mail.com -s "test multiple recivers"
  -t to@mail.com -s "test display with a fake from_addr -f fake@mail.com
  -t to@mailcom -s "test cc and bcc" -cc cc@mail.com -bcc bcc@mail.com
  -t to@mail.com -s "test attachments" -a README.md -a requirements.txt 
''', fg='yellow')

@click.command(
    name='send',
    help='send email to user(s)',
    no_args_is_help=True,
    epilog=__epilog__,
)
@click.option('-f', '--from-addr', help='the display address of the sender, default is the login username')
@click.option('-t', '--to-addrs', help='the recipient address(es)', multiple=True, required=True)
@click.option('-s', '--subject', help='the subject of the email', required=True)
@click.option('-b', '--body', help='the body of the email')
@click.option('-a', '--attachments', help='the attachments of the email', multiple=True)
@click.option('-C', '--charset', help='the charset of the email', default='utf-8', show_default=True)
@click.option('-c', '--content-type', help='the content type of the email, eg.: plain, html', default='plain', show_default=True)
@click.option('-cc', '--cc', help='the cc address(es)', multiple=True)
@click.option('-bcc', '--bcc', help='the bcc address(es)', multiple=True)
@click.pass_obj
def main(obj, **kwargs):
    main_kwargs = obj['main_kwargs']

    try:
        mail = SendEmail(**main_kwargs)
    except ValidationError as e:
        click.secho(f'[SmtpConfigError] missing required arguments as follow:', fg='red')
        print(e)

        if click.confirm('Do you want to complete a configration?'):
            initialize_config(**main_kwargs)
            if click.confirm('Save your configration?'):
                _env_file = main_kwargs.get('_env_file')
                mail.save_config(env_file=_env_file)
                click.secho(f'Configration saved to: {_env_file}', fg='green')
        else:
            exit(1)

    try:
        mail.login()
    except LoginError as e:
        click.secho(f'[LoginError] {e}', fg='red')
        click.secho('please check your payload:')
        print(mail.model_dump_json(indent=2))
        exit(2)

    mail.send(**kwargs)
    mail.close()
