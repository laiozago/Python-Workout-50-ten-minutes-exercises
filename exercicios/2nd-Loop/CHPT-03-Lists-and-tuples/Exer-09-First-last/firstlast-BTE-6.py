"""
Write a function that partly emulates the built-in zip function (http://mng.bz/ Jyzv),
taking any number of iterables and returning a list of tuples. Each tuple will contain
one element from each of the iterables passed to the function. Thus, if I call
myzip([10, 20,30], 'abc'), the result will be [(10, 'a'), (20, 'b'), (30, 'c')]. You can return
a list (not an iterator) and can assume that all the iterables are of the same length.
"""


def myzip(lst_1, lst_2):
    resultado = []
    for i in range(len(lst_1)):
        tpla = (lst_1[i], lst_2[i])
        resultado.insert(i, tpla)
    return resultado


print(myzip([10, 20, 30], 'abc'))
