def pig_latin():
    word = input("palavra para traduzir: ")
    word.lower()
    if word[0] in 'aeiou':
        new_word = word + 'way'
        return new_word
    else:
        new_word = word[1:] + word[0] + 'ay'
        return new_word


print(pig_latin())