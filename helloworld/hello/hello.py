import helloworld.hello.hello_helpers as helpers

def get_greeting(languages, default_lang):
    prefix = helpers.get_prefix()
    greeting = languages[default_lang]
    return f"{prefix} {greeting}"


