# E9_DAPP

import pyfiglet
from colorama import Fore

print(Fore.LIGHTGREEN_EX)
result = pyfiglet.figlet_format("Daniel Alfonso Pirir Perez", font="shadow")
print(result)

def count_words(text):

    text = text.split()
    palabras = {}
    for i in text:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras

def most_repeated(palabras):
    max_palabra = ''
    max_frekuencia = 0
    for palabra, frekuencia in palabras.items():
        if frekuencia > max_freq:
            max_word = palabra
            max_freq = frekuencia
    return max_palabra, max_frekuencia

text = 'Y yo llegué a la grasa temblando de miedo y te perdí perdón porque no soy el pepe, te confesé que no soy en niño del oxxo :v'
print(count_words(text))
print(most_repeated(count_words(text)))