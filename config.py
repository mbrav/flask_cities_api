from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    admin_email: str = "admin@example.com"
    param_folder: str = "param"
    result_folder: str = "output"

    class Config:
        env_prefix = "APP_"


@lru_cache()
def get_setting():
    return Settings()
