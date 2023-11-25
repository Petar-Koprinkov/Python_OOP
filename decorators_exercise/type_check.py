def type_check(parameter_type):
    def decorator(function):
        def wrapper(parameter):
            if not isinstance(parameter, parameter_type):
                return "Bad Type"
            return function(parameter)
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
