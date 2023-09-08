from pathlib import Path

import dotenv
from pydantic import Field
from pydantic_settings import BaseSettings


class SMTP_Config(BaseSettings):
    """
    SMTP_Config is a class for storing and managing SMTP configurations.
    
    Attributes:
        host (str): The address of the SMTP server.
        port (int): The port number for the SMTP server, default is 465.
        username (str): The username for SMTP authentication.
        password (str): The password for SMTP authentication.
        use_ssl (bool): Flag indicating if SSL should be used.
    """
    
    host: str = Field(..., env='SMTP_HOST', alias='SMTP_HOST')
    port: int = Field(default=465, env='SMTP_PORT', alias='SMTP_PORT')
    username: str = Field(..., env='SMTP_USERNAME', alias='SMTP_USERNAME')
    password: str = Field(..., env='SMTP_PASSWORD', alias='SMTP_PASSWORD')
    use_ssl: bool = Field(..., env='SMTP_USE_SSL', alias='SMTP_USE_SSL')

    def __init__(self, env_file='~/.mailkit.env', **data):
        """
        Constructor for initializing from an environment file.
        
        Args:
            env_file (str): Path to the environment file, defaults to '~/.mailkit.env'.
            data (dict): Additional initialization parameters.
        """
        env_file = Path(env_file).expanduser()
        values = dotenv.dotenv_values(env_file)
        if values:
            print(f'Loaded env file: {env_file}')
        super().__init__(**{**values, **data})
        self._env_file = env_file

    def save_config(self):
        """
        Save the current settings to the environment file.
        """
        with self._env_file.open('w') as out:
            for key, value in self.model_dump(by_alias=True).items():
                out.write(f'{key}={value}\n')
        print(f'Updated env file: {self._env_file}')


if __name__ == '__main__':
    settings = SMTP_Config(SMTP_HOST='smtp.qq.com')
    print(settings.model_dump())
    settings.save_config()
