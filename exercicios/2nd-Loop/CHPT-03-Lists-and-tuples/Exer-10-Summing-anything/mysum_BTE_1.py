"""
Write a function, mysum_bigger_than, that works the same as mysum, except that it takes a first
argument that precedes *args. That argument indicates the threshold for including an argument
in the sum. Thus, calling mysum_bigger_than(10, 5, 20, 30, 6) would return 50
— because 5 and 6 aren’t greater than 10. This function should similarly work with
any type and assumes that all of the args are of the same type. Note that > and < work
on many different types in Python, not just on numbers; with strings, lists, and tuples,
it refers to their sort order.
"""


def my_sum_bigger_than(num, *items):
    if not num or not items:
        return None

    # Encontrar a posição do primeiro número maior que num
    index_of_first_bigger = -1
    for i, item in enumerate(items):
        if item > num:
            index_of_first_bigger = i
            break

    # Se nenhum número for maior que num, retornar None
    if index_of_first_bigger == -1:
        return None

    # Iniciar 'resultado' com o valor do primeiro número maior que num
    resultado = items[index_of_first_bigger]

    # Iterar por items a partir da posição do maior e adicionar ao resultado se for maior que num
    for item in items[index_of_first_bigger + 1:]:
        if item > num:
            resultado += item

    return resultado


print(my_sum_bigger_than(10, 20, 30, 40))
print(my_sum_bigger_than('b', 'a', 'b', 'c', 'd'))
print(my_sum_bigger_than([50, 20, 30], [40, 50, 60], [70, 80]))
print(my_sum_bigger_than(10, 5, 3, 10, 20, 30))
