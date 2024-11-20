from shared.some_postgres import SomeRepo


class FirstPackage:
    def __init__(
        self,
        some_repo: SomeRepo,
    ):
        self._some_repo = some_repo

    def nu_tipa(
        self,
        param_one: str,
    ) -> tuple[str, int]:
        print("Hi! It's First Package")
        x = self._some_repo.hello()
        print(
            f"i got a param = {param_one} and injected(or maybe not injected)[definitely not cuz i am not in the wiring targets] repo gave me {x}, returning the tuple"
        )
        return param_one, x
