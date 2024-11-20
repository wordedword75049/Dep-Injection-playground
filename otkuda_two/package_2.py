from dependency_injector.wiring import inject


class SecondPackage:
    @inject
    def __init__(
        self,
        some_secret_int: int,
    ):
        self._some_secret_int = some_secret_int

    def nu_tipa_too(
        self,
        param_one: str,
    ) -> tuple[str, int]:
        print("Hi! It's Second Package")
        print(
            f"i got a param = {param_one} and i have inside me a secret int(which was given to me in container) = {self._some_secret_int}, returning the tuple"
        )
        return param_one, self._some_secret_int
