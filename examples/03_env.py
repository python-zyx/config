from zyx.config import BaseConfig


class Config(BaseConfig):
    name: str = "World"


config = Config("hello.toml", create=True, env_prefix="ZYX")


print(f"Hello, {config.name}!")
