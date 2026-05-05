# E7_DAPP

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

print(cuadrado([5, 6, 7, 8, 9]))
print(cuadrado([2.2, 5.8, 5.2, 7.5, 14.68, 7.6]))