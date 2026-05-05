#E1 DAPP

import pyfiglet
from colorama import Fore
print(Fore.LIGHTGREEN_EX)
result = pyfiglet.figlet_format("Daniel Alfonso Pirir Perez", font="shadow")
print(result)


#Función sin parámentros y sin retorno
def saludar():
    print("¡Hola amiga!")

#Llamada a la funion
print("Funcion 1")
saludar()