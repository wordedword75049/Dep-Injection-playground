from dependency_injector import containers, providers

import kuda as kuda
import otkuda_three as otkuda_three
from otkuda_one.package_1 import FirstPackage
from otkuda_one.subcontainer_one import FirstSubcontainer
from otkuda_three.package_3 import ThirdPackage
from otkuda_two.package_2 import SecondPackage
from shared.shared_container import SharedSubcontainer
from shared.some_postgres import SomeRealPGRepo

SECRET_CONST = 3


class ApplicationContainer(containers.DeclarativeContainer):
    # wiring_config = containers.WiringConfiguration(
    #     packages=[
    #         kuda,
    #         otkuda_three,
    #     ]
    # )
    config = providers.Configuration()
    some_repo = providers.Singleton(SomeRealPGRepo, inner_config=config.postgres_config)

    #shared_subcontainer = providers.Container(SharedSubcontainer, config=config.postgres_config)

    # first_subcontainer = providers.Container(
    #     FirstSubcontainer,
    #     some_repo=shared_subcontainer.some_repo,
    # )

    first_package = providers.Singleton(FirstPackage, some_repo=some_repo)
    second_package = providers.Singleton(SecondPackage, some_secret_int=SECRET_CONST)
    third_package = providers.Singleton(ThirdPackage)

