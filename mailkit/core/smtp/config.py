from typing import List, Union, Optional
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class SmtpConfig(BaseSettings):
    host: str
    port: Optional[int] = None
    username: str
    password: str
    use_ssl: bool = True
    use_tls: bool = False
    timeout: int = 10

    model_config = SettingsConfigDict(
        env_file='~/.mailkit.env',
        env_prefix='SMTP_',
        case_sensitive=False
    )

    def save_config(self, env_file=None):
        env_file = env_file or self.model_config.get('env_file')
        prefix = self.model_config.get('env_prefix')
        with Path(env_file).expanduser().open('w') as f:
            for k, v in self.model_dump().items():
                f.write(f'{prefix}{k.upper()}={v}\n')


if __name__ == '__main__':
    # s = SmtpConfig(host='smtp.gmail.com')
    # s.save_config('out.env')

    s = SmtpConfig(_env_file='out.env')
    print(s.model_dump())