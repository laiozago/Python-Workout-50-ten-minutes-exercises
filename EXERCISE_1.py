import random
from pprint import pprint


def guess_the_number():
    num_gen = random.randint(0, 100)
    print(num_gen)
    while True:
        guess = int(input('Entre um numero inteiro entre 0 e 100: '))
        if int(guess) != num_gen:
            if int(guess) > num_gen:
                pprint('Errou! Seu palpite foi muito alto.')
            if int(guess) < num_gen:
                pprint('Errou! Seu palpite foi muito baixo.')
        if int(guess) == num_gen:
            pprint('Parabens! Acertou.')
            return


guess_the_number()
