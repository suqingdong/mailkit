from pathlib import Path

import click

from mailkit.core.smtp import SendEmail


def initialize_config(**kwargs):
    host = click.prompt('>>> SMTP host', default=kwargs.get('host'))
    port = click.prompt('>>> SMTP port', default=kwargs.get('port', 465))
    username = click.prompt('>>> SMTP username', default=kwargs.get('username'))
    password = click.prompt('>>> SMTP password', default=kwargs.get('password'), hide_input=True)
    use_ssl = click.prompt('>>> SMTP use ssl', default=kwargs.get('use_ssl'), type=bool)
    timeout = click.prompt('>>> SMTP timeout', default=kwargs.get('timeout'), type=int)

    mail = SendEmail(host=host,
                     port=port,
                     username=username,
                     password=password,
                     use_ssl=use_ssl,
                     timeout=timeout)
    try:
        mail.login()
        return mail
    except Exception as e:
        click.echo(f'>>> Error: {e}')
        return False


@click.command(
    name='config',
    help='initialize the configuration file',
)
@click.pass_obj
def main(obj):
    main_kwargs = obj['main_kwargs']
    env_file = main_kwargs['_env_file']
    if Path(env_file).expanduser().is_file():
        if not click.confirm(f'`{env_file}` already exists, do you want to overwrite it?'):
            return
    
    if mail := initialize_config(**main_kwargs):
        
        mail.save_config(env_file=env_file)
        click.secho(f'Saved configuration to {env_file}', fg='green')
        mail.close()
    else:
        click.secho('>>> Error: SMTP login failed', fg='red')
