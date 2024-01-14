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


# Chama a função e armazena o resultado
resultado = run_timing()

# Verifica se a função retornou um resultado válido antes de imprimir
if resultado is not None:
    print(f"A média de quilômetros por dia é {resultado:.2f}")
