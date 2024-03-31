from functools import reduce

def multiply_list(lst):
    return reduce(lambda x, y: x*y, lst)

numbers = [2, 3, 4]
print(multiply_list(numbers))