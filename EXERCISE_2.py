def my_sum(*args):
    total_sum = 0
    for x in args:
        total_sum += x
    return total_sum


# print(my_sum(1, 2, 3))


# BEYOND

def my_sum_v02(lista, num):
    total_sum = int(num)
    for x in lista:
        if isinstance(x, list):
            total_sum += my_sum_v02(x, 0)  # Recursively sum elements of nested list
        else:
            try:
                total_sum += x
            except TypeError:
                print(f"Ignoring: {x}")
    return total_sum


# my_list = [1, 2, [3, 4, [5, 6]], 7, 8]
# result = my_sum_v02(my_list, 2)
# print(result)


def my_sum_v03(*args):
    total_sum = 0

    for arg in args:
        if isinstance(arg, list):
            total_sum += my_sum_v03(*arg)  # Recursively sum elements of nested list
        elif isinstance(arg, (int, float)):
            total_sum += arg
        else:
            print(f"Ignoring: {arg}")

    return total_sum


# result = my_sum_v03(1, 2, [3, 4, [5, 6]], 7, 8, "not a number", [9, "ignore me"])
# print(result)


def average(lista):
    soma = 0
    cont = 0
    for x in lista:
        try:
            soma += float(x)
            cont += 1
        except ValueError:
            print(f'O valor "{x}" não é um número válido e será ignorado.')

    if cont == 0:
        print("Nenhum número válido encontrado na lista.")
        return None

    media = soma / cont
    return media


valor = average([1, 2, "a", 3, 4])
print(f"A média é {valor}")
