
# from helloworld.hello import hello
import helloworld.hello.hello as hello

def get_postfix():
    return "postfix"


# Added to test a main method for the case I want to call a 
# module directly from command line, like:
#
# > python_project_template$ python -m helloworld.world.world_helpers 
#
if __name__ == "__main__":
    print("I improte the helloworld.hello.hello module from here: ")
    print(hello.__file__)
    import sys
    print("sys.path is:")
    print(sys.path)
    try:
        name = sys.argv[1]
    except IndexError:
        name = "You can give your name as an argument."

    print("Hello ", name)
    print("I will now call the get_postfix() function, which should "
            "return the word 'postfix'")
    print(get_postfix())


