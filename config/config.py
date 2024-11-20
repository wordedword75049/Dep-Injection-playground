from typing import Set

from pydantic import (
    Field,
)
from pydantic_settings import BaseSettings


class PostgresConfig(BaseSettings, case_sensitive=False, env_prefix="postgres_"):
    # model_config = SettingsConfigDict(env_prefix='postgres_')
    host: str = Field()
    port: int = Field(default=50410)
    user: str = Field(default="user")
    password: str = Field(default="password")
    database_name: str = Field(default="database")
    extensions: Set[str] = set()


class Config(BaseSettings):
    postgres_config: PostgresConfig = PostgresConfig()


print(Config().model_dump())
