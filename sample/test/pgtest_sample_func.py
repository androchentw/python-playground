def equal(param1, param2):
    return param1 == param2


def hello(text, **kwargs):
    name = kwargs.get("name", "username")
    return f"hello: {text}~ {name}."
