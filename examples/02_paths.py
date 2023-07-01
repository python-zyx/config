from zyx.config import BaseConfig, ConfigPaths


class Config(BaseConfig):
    name: str = "World"


config = Config("hello.toml", create=True, paths=ConfigPaths("example"))


print(f"Config file lookup paths: {config.paths}")
print(f"Config file path: {config.path}")
print(f"Hello, {config.name}!")
