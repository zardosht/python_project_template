import toml

from helloworld.hello import hello
from helloworld.world import world

"""
Docs for `app.py`. :D 8)
"""

def read_config(configfile): 
    """
    Rreds the given TOML config file and returns a config dictionary.

    Args:
        configfile (str): Path to the TOML config file. 

    Returns:
        dictionary: Config dictionary loaded and parsed using `toml` 
        module. 
    """    
    return toml.load(configfile)


def say_hello():
    config = read_config("conf/config.toml")
    default_lang = config["default_lang"]
    greetings = config["language"]
    greeting = hello.get_greeting(greetings, default_lang)
    world.say_hello(greeting)
    


