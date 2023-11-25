def tags(parameter):
    def decorator(function):
        def wrapper(*args, **kwargs):
            return f"<{parameter}>{function(*args)}</{parameter}>"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
