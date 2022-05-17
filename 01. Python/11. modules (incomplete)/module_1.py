
# add function
def add_test (*args):
    """you can add any number of int values"""
    sum = 0
    for i in args:
        sum = sum + i
        return sum
# multiply function
def multiply_test (*args):
    """you can add any number of int values"""
    mul = 1
    for i in args:
        mul = mul * i
    return mul

# division function
def division_test (*args):
    """you can add any number of int values"""
    div = 1
    for i in args:
        div = i/div
    return div

#print
def display():
    print("this is the module: ",__name__)
