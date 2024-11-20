import kuda as kuda
import otkuda_three as otkuda_three
from config.config import Config
from container import ApplicationContainer


# config_obj: Config
def inject_dependencies() -> ApplicationContainer:
    json_config = Config().model_dump(mode="json")

    container = ApplicationContainer()

    container.config.from_dict(json_config)
    container.wire(
        packages=[
            kuda,
            otkuda_three,
        ]
    )

    return container
