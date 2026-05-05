#E3_DAPP

import pyfiglet
from colorama import Fore
print(Fore.LIGHTGREEN_EX)
result = pyfiglet.figlet_format("Daniel Alfonso Pirir Perez", font="shadow")
print(result)

def factoriales(n):
    elpollo = 1
    for i in range(n):
        elpollo *= i+1
    return elpollo

print(factoriales(6))
print(factoriales(67))