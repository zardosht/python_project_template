import helloworld.world.world_helpers as helpers

def say_hello(greeting):
    postfix = helpers.get_postfix()
    hello = f"{greeting} World! {postfix}"
    print(hello)
    return hello

