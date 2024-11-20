from src.shared.infra.persistence.database.sqlalchemy_mixin import SQLAlchemyMixin


class SomeRepo:
    def hello(self) -> int:
        ...


class SomeRealPGRepo(SomeRepo):
    def __init__(self, inner_config):
        self.inner_config = inner_config

    def hello(self) -> int:
        print("Hello from SomeRealPGRepo")
        print(f"my config is {self.inner_config['host']}-{self.inner_config['port']}-{self.inner_config['user']}-{self.inner_config['password']}-{self.inner_config['database_name']}")
        print("returning 1 just for fun")
        return 1
