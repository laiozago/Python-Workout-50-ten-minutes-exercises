"""
Write a function that takes a list or tuple of numbers. Return a two-element list,
containing (respectively) the sum of the even-indexed numbers and the sum of the odd-indexed numbers.
So calling the function as even_odd_sums([10, 20, 30, 40, 50, 60]), you’ll get back [90, 120].
"""


def even_odd_sums(lst):
    sums = [0, 0]  # IMPORTANTE: A lista deve ser iniciada com valores
    for i in range(len(lst)):
        if i % 2 == 0:
            sums[0] += lst[i]
        else:
            sums[1] += lst[i]
    return sums


try:
    resultado = even_odd_sums([1, 2, 3, 4, 5, 6])
    print(resultado)
except TypeError:
    print("A lista deve conter apenas números")
