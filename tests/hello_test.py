import pytest
import toml

from helloworld.hello import hello



@pytest.fixture
def config():
    config = toml.load("conf/config-test.toml")
    return config


def test_get_greeting(config):
    def_lang = config["default_lang"]
    greeting = hello.get_greeting(config["language"], def_lang)
    assert(greeting == "prefix Servus")

