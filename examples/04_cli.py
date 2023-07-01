import click
from zyx.config import BaseConfig


class Config(BaseConfig):
    name: str = "World"


config = Config("hello.toml", create=True)


@click.command()
@click.option("--name")
@config.click_options
def main(name: str):
    assert name == config.name
    print(f"Hello, {config.name}!")


main()
