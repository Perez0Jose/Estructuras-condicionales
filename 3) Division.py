#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no

import os

num1 = int(input("Ingrese el diviendo"))
num2 = int(input("Ingrese el divisor"))


if num1 % num2 == 0 or num2 % num1 == 0:
     print("su division es exacta")
else:
    print("Su division no es exacta")

print()

