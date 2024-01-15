def run_timing():
    soma_kms = 0  # Soma total de quilômetros percorridos
    dias = 0  # Número de dias

    while True:
        num = input('Qual é o número de quilômetros? (Deixe em branco para finalizar) ')

        if not num:
            if dias == 0:
                print("Nenhum dado inserido. Não é possível calcular a média.")
                return None  # Retorna None para indicar que não foi possível calcular a média
            media = soma_kms / dias
            return media  # Retorna a média

        try:
            kms = float(num)
            if kms < 0:
                print("Por favor, insira um valor positivo.")
            else:
                soma_kms += kms
                dias += 1
        except ValueError:
            print("Por favor, insira um valor numérico válido.")


# resultado = run_timing()
# if resultado is not None:
# print(f"A média de quilômetros por dia é {resultado:.2f}")


def get_name():
    while True:
        nome = input("Entre seu nome: ")  # obter nome
        if nome.isalpha():
            return nome
        else:
            print("Por favor, insira um nome válido (sem números ou caracteres especiais).")


def print_triangle(nome):
    for index, letter in enumerate(nome):  # imprimir o triangulo
        print(nome[:index + 1])


def name_triangle():
    print("Bem-vindo ao Triângulo de Nomes!")
    nome = get_name()
    print_triangle(nome)


#name_triangle()
