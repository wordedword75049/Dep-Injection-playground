from dependency_injector import containers, providers

from shared.some_postgres import SomeRealPGRepo


class SharedSubcontainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    some_repo = providers.Singleton(SomeRealPGRepo, inner_config=config)
