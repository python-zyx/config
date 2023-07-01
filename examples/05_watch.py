import time
from zyx.config import BaseConfig


class Config(BaseConfig):
    name: str = "World"


config = Config("hello.toml", create=True, watch=True)


@config.on_change("name")
def on_name_updated(old: str, new: str):
    print(f"Name changed from {old} to {new}")
    print(f"Hello, {config.name}!\n\n")


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
