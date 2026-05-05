# E8_DAPP

import pyfiglet
from colorama import Fore

print(Fore.LIGHTGREEN_EX)
result = pyfiglet.figlet_format("Daniel Alfonso Pirir Perez", font="shadow")
print(result)


def cuadrado(lista):

    list = []
    for i in lista:
        list.append(i**2)
    return list

def medida_de_variacion(lista):
    coso = {}
    coso['media'] = sum(lista)/len(lista)
    coso['varianza'] = sum(cuadrado(lista))/len(lista)-coso['media']**2
    coso['desviacion tipica'] = coso['varianza']**0.5
    return coso

print(medida_de_variacion([1, 2, 3, 4, 5]))
print(medida_de_variacion([2.3, 8.9, 6.9, 2.56, 3.67, 89.6]))