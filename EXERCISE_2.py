def my_sum(*args):
    total_sum = 0
    for x in args:
        total_sum += x
    return total_sum


print(my_sum([1, 2, 3]))
