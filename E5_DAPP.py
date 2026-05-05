#E5_DAPP

import pyfiglet
from colorama import Fore
print(Fore.LIGHTGREEN_EX)
result = pyfiglet.figlet_format("Daniel Alfonso Pirir Perez", font="shadow")
print(result)

def circulo_area(radio):
    pi = 3.1415
    return pi*radio**2

def volumen_cilindro(radio, altura):
    return circulo_area(radio)*altura

print(volumen_cilindro(42,149))