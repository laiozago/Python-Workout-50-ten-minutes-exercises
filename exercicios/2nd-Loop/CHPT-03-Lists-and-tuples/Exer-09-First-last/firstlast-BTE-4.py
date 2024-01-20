"""
Write a function that takes a list or tuple of numbers. Return the result of alternately adding and subtracting numbers
from each other. So calling the function as plus_minus([10, 20, 30, 40, 50, 60]),
you’ll get back the result of -10+20-30+40-50+60, or 30.
"""


def plus_minus(lst):
    even_sum = sum(lst[i] for i in range(0, len(lst), 2))
    odd_sum = sum(lst[i] for i in range(1, len(lst), 2))
    return odd_sum - even_sum


print(plus_minus([10, 20, 30, 40, 50, 60]))
