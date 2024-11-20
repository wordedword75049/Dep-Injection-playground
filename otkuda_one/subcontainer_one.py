from dependency_injector import containers, providers

from otkuda_one.package_1 import FirstPackage


class FirstSubcontainer(containers.DeclarativeContainer):
    some_repo = providers.Dependency()
    first_package = providers.Singleton(FirstPackage, some_repo=some_repo)
