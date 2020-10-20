import toml


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
