
'''
Write a function, mysum_bigger_than, that works the same as mysum, except that it takes a first
argument that precedes *args. That argument indicates the threshold for including an argument
in the sum. Thus, calling mysum_bigger_than(10, 5, 20, 30, 6) would return 50
— because 5 and 6 aren’t greater than 10. This function should similarly work with
any type and assumes that all of the args are of the same type. Note that > and < work
on many different types in Python, not just on numbers; with strings, lists, and tuples,
it refers to their sort order.
'''
