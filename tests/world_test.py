import pytest
import toml

from helloworld.world import world


@pytest.fixture
def greeting():
    return "Hi"
    # return "Servus"
    # return "Aloha"


def test_say_hello(greeting):
    hello = world.say_hello(greeting)
    assert(hello == "Hi World! postfix")

