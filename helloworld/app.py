import toml

from helloworld.hello import hello
from helloworld.world import world

"""
Docs for `app.py`. :D 8)
"""

def read_config(configfile):
    """Reads the given config file and returns the config dictionary. 

    :param configfile: The path to the `config.toml` files. Path must be
                       relative to the `os.getcwd()`
                        
    :type configfile: string
    :return: The config dictionary loaded and parsed using `toml` module.
    :rtype: dictionary
    """  
    return toml.load(configfile)


def say_hello():
    config = read_config("conf/config.toml")
    default_lang = config["default_lang"]
    greetings = config["language"]
    greeting = hello.get_greeting(greetings, default_lang)
    world.say_hello(greeting)
    


