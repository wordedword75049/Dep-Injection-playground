from typing import Set, List, Dict, Any

from pydantic import Field, PostgresDsn, RedisDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresConfig(BaseSettings, case_sensitive=False, env_prefix="postgres_"):
    # model_config = SettingsConfigDict(env_prefix='postgres_')
    host: str = Field(default="localhost")
    # hostbrr: str
    port: int
    try_bool: bool
    user: str = Field(default="user")
    password: str = Field(default="password")
    database_name: str = Field(default="database")
    extensions: List[str] = []
    kinda: Dict[str, Any] = {}

    @computed_field
    @property
    def pg_dsn(self) -> PostgresDsn:
        return PostgresDsn.build(
            host=self.host,
            port=self.port,
            path=self.database_name,
            username=self.user,
            password=self.password,
            scheme="public",
        )  # f"postgres://{user}:{password}@{host}:{port}/{database_name}"

    @computed_field
    @property
    def redis_dsn(self) -> RedisDsn:
        return RedisDsn.build(host=self.host, port=self.port, password=self.password, scheme="redis")


class NewConfig(BaseSettings, case_sensitive=False, env_prefix="new_"):
    # model_config = SettingsConfigDict(env_prefix='postgres_')
    host: str = Field()


class Config(BaseSettings):
    postgres_config: PostgresConfig = PostgresConfig()
    model_config = SettingsConfigDict(env_prefix="try_")
    x: int = Field()
    lowcase: str = Field(alias="highcase")


x1 = Config()
# print(f"postgres://{x.user}:{x.password}@{x.host}:{x.port}/{x.database_name}")
# print(PostgresDsn.build(host=x.host, port=x.port, path=x.database_name, username=x.user, password=x.password, scheme="public"))
print(x1.model_dump())
