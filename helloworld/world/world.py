import helloworld.world.world_helpers as helpers

def say_hello(greeting):
    postfix = helpers.get_postfix()
    hello = f"{greeting} World! {postfix}"
    print(hello)
    return hello


def load_data(path):
    with open(path, "r") as f:
        my_str = f.read()
        print(my_str)

