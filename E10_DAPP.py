# E9_DAPP

import pyfiglet
from colorama import Fore

print(Fore.LIGHTGREEN_EX)
result = pyfiglet.figlet_format("Daniel Alfonso Pirir Perez", font="shadow")
print(result)
def to_decimal(n):

    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

def to_binary(n):

    binario = []
    while n > 0:
        binario.append(str(n % 2))
        n //= 2
    binario.reverse()
    return ''.join(binario)

print(to_decimal('10011'))
print(to_binary(50))
print(to_decimal(to_binary(67)))
print(to_binary(to_decimal('1110')))
