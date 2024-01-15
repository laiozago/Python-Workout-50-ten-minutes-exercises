def pig_latin(word):
    is_upper = word[0].isupper()  # Verifica se a primeira letra é maiúscula
    word = word.lower()  # Converte a palavra para minúsculas para aplicar as regras

    # Separa a pontuação da palavra
    punc = ''
    while word and word[-1].isalpha() is False:
        punc = word[-1] + punc
        word = word[:-1]

    if word and word[0] in 'aeiou':
        new_word = word + 'way'
    else:
        new_word = word[1:] + word[0] + 'ay'

    # Adiciona a pontuação de volta à palavra
    new_word += punc

    # Mantém a capitalização original
    if is_upper:
        new_word = new_word.capitalize()

    return new_word

def pig_latin_sentence():
    frase = input('Entre a frase que deseja traduzir: ')
    palavras = frase.split()
    novas_palavras = []
    for palavra in palavras:
        novas_palavras.append(pig_latin(palavra))
    print(' '.join(novas_palavras))

# Chamada da função principal
pig_latin_sentence()
