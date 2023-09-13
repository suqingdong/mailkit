from pathlib import Path

import click

from mailkit import version_info
from ._send import main as send_cli
from ._config import main as config_cli


CONTEXT_SETTINGS = dict(help_option_names=['-?', '-h', '--help'])

__epilog__ = click.style(
    'Contact: {author} <{author_email}>',
    bold=True,
    fg='white'
).format(**version_info)


@click.group(
    name=version_info['prog'],
    help=click.style(version_info['desc'], italic=True, fg='cyan', bold=True),
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
    epilog=__epilog__,
)
@click.version_option(version=version_info['version'],
                      prog_name=version_info['prog'],
                      message=click.style('%(prog)s, version %(version)s', bold=True, fg='green'))
@click.option('-H', '--host', help='SMTP server hostname or IP address')
@click.option('-P', '--port', help='SMTP server port', type=int)
@click.option('-u', '--username', help='SMTP server username')
@click.option('-p', '--password', help='SMTP server password')
@click.option('-s', '--use-ssl', help='Use SSL connection', type=bool, default=True, show_default=True)
@click.option('-t', '--timeout', help='SMTP server timeout', type=int, default=10, show_default=True)
@click.option('-e', '--env-file', help='The environment file to load', type=str, default='~/.mailkit.env', show_default=True)
@click.pass_context
def cli(ctx, **kwargs):
    ctx.ensure_object(dict)
    ctx.obj['main_kwargs'] = dict(
        _env_file=kwargs.pop('env_file'),
        **{k: v for k, v in kwargs.items() if v is not None}
    )


def main():
    cli.add_command(send_cli)
    cli.add_command(config_cli)
    cli()


if __name__ == '__main__':
    main()
