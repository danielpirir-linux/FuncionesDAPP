#E4_DAPP

import pyfiglet
from colorama import Fore
print(Fore.LIGHTGREEN_EX)
result = pyfiglet.figlet_format("Daniel Alfonso Pirir Perez", font="shadow")
print(result)

def iva(monto, porcentaje=21):
    return monto + monto*porcentaje/100

print(iva(1000,10))
print(iva(1000))