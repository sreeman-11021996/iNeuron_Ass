def exp_num(num):
    def exp_calc(func):
        def wrapper(x, y):
            return [val ** num for val in func(x, y)]
        return wrapper
    return exp_calc


@exp_num(3)
def return_list(val1, val2):
    return range(val1 + 1, val2)


print(return_list(2, 10))
