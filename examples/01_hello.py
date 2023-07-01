from zyx.config import BaseConfig


class Config(BaseConfig):
    name: str = "World"


config = Config("hello.toml", create=True)


print(f"Hello, {config.name}!")
