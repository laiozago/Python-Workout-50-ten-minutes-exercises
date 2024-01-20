"""
Handle capitalized words—If a word is capitalized (i.e., the first letter is capitalized,
but the rest of the word isn’t), then the Ubbi Dubbi translation should be similarly capitalized.
"""


def ubbi_dubbi_v2(palavra):
    global palavra_em_minusculas
    titulo = False
    if palavra[0] in "AEIOU":
        palavra_em_minusculas = palavra.lower()
        titulo = True
    lista_palavra = list(palavra_em_minusculas)
    for i in range(len(lista_palavra)):
        if lista_palavra[i] in "aeiou":
            lista_palavra[i] = "ub" + lista_palavra[i]
    resultado = ''.join(lista_palavra)
    if titulo:
        return resultado.capitalize()
    return resultado


print(ubbi_dubbi_v2('Alberto'))