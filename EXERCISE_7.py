# In Ubbi-Dubbi every vowel is preceded with ub
def ubbi_dubbi(strn):
    # transformar palavra em lista
    palavra_lista = list(strn)
    # indentificar a posição das vogais e adicionar ub antes das vogais
    for i in range(len(palavra_lista)):
        if palavra_lista[i] in "aeiou":
            palavra_lista[i] = "ub" + palavra_lista[i]
    # tranformar lista em string
    resultado = ''.join(palavra_lista)
    # retornar palavra
    return resultado


def ubbi_dubbi_txt(txt):
    text_to_list = str(txt).split()
    for i in range(len(text_to_list)):
        text_to_list[i] = ubbi_dubbi(text_to_list[i])
    resultado = ' '.join(text_to_list)
    return resultado


print(ubbi_dubbi_txt('laio dos santos zago passos'))
