from dependency_injector.wiring import Provide, inject

from otkuda_one.package_1 import FirstPackage
from otkuda_three.package_3 import ThirdPackage
from otkuda_two.package_2 import SecondPackage


class CoolClass:
    @inject
    def do_smth(
        self,
        first_package: FirstPackage = Provide["first_package"],
    ) -> tuple[str, int]:
        print("Hi, its CoolClass. I now will call the method from first injected package")
        one, two = first_package.nu_tipa("wow")
        print(f"Injected package 1 gave me this thing - {one, two}")
        return one, two

    @inject
    def do_smth_second_time(
        self,
        second_package: SecondPackage = Provide["second_package"],
    ) -> tuple[str, int]:
        print("Hi, its CoolClass again. I now will call the method from second injected package")
        one, two = second_package.nu_tipa_too("wow again")
        print(f"Injected package 2 gave me this thing - {one, two}")
        return one, two

    @inject
    def do_smth_third_time(
        self,
        third_package: ThirdPackage = Provide["third_package"],
    ) -> tuple[str, int]:
        print(
            "Hi, its CoolClass once again. I now will call the method from third injected package(which has injection in it)"
        )
        one, two = third_package.nu_tipa_three("THIRD TIME OMG")
        print(f"Injected package 3 gave me this thing - {one, two}")
        print(self.__class__.__name__)
        return one, two
