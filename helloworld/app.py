from helloworld import utils
from helloworld.hello import hello
from helloworld.world import world

"""
Docs for `app.py`. :D 8)
"""


def say_hello():
    config = utils.read_config("conf/config.toml")
    default_lang = config["default_lang"]
    greetings = config["language"]
    greeting = hello.get_greeting(greetings, default_lang)
    world.say_hello(greeting)

    world.load_data("data/dummy.txt")
    


if __name__ == "__main__":
    say_hello()

