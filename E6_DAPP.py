#E6_DAPP

import pyfiglet
from colorama import Fore
print(Fore.LIGHTGREEN_EX)
result = pyfiglet.figlet_format("Daniel Alfonso Pirir Perez", font="shadow")
print(result)

def muestra(lista):
    return sum(lista)/len(lista)

print(muestra([6, 7, 8, 9, 10]))
print(muestra([6.3, 8.7, 6.8, 10.7, 13.1, 16.6]))