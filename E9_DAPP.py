# E9_DAPP

import pyfiglet
from colorama import Fore

print(Fore.LIGHTGREEN_EX)
result = pyfiglet.figlet_format("Daniel Alfonso Pirir Perez", font="shadow")
print(result)

def mcd(n, m):
    residuo = 0
    while(m > 0):
        residuo = m
        m = n % m
        n = residuo
    return residuo

def mcm(n, m):
    if n > m:
        multiplo = n
    else:
        multiplo = m
    while (multiplo % n != 0) or (multiplo % m != 0):
        multiplo += 1
    return multiplo

print(mcd(36,45))
print(mcm(72,81))