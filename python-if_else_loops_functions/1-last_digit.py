#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ultimo_digito = abs(number) % 10
print(f"El último dígito de {number} es {ultimo_digito}")
if ultimo_digito > 5:
    print(" y es mayor que 5")
elif ultimo_digito == 0:
    print(" y es 0")
else:
    print(" y es menor que 6 y no es 0")
