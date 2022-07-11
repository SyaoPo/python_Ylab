def my_decorator(func):
    my_dict = {}

    def wrapper(*args, **kwargs):
        key = int(*args)
        if key in my_dict.keys():
            return my_dict[key]
        result = func(*args, **kwargs)
        my_dict[key] = result
        return result

    return wrapper


@my_decorator
def multiplier(number: int):
    return number * 2
