from dependency_injector.wiring import Provide, inject

from shared.some_postgres import SomeRepo


class ThirdPackage:
    @inject
    def nu_tipa_three(
        self,
        param_one: str,
        some_repo: SomeRepo = Provide["some_repo"],
    ) -> tuple[str, int]:
        print("Hi! It's Third Package")
        x = some_repo.hello()
        print(
            f"i got a param = {param_one} and injected [100% injected, cuz added to wiring target] repo gave me {x}, returning the tuple"
        )
        return param_one, x
