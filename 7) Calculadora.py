#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.
#El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.
#La salida del programa debe ser el resultado de la operación.


num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))
op = print("""Ingrese un op: 
           1)SUMA
           2)RESTA
           3)MULTIPLICACION
           4)DIVISION
           5)EXPONENCIACION
       """)
eleccion = int(input())


if eleccion== 1:
    S = (num1 + num2)
    print(f"El resultado es {S}")
elif eleccion == 2:
    R = (num1 - num2)
    print(f"El resultado es {R}")
elif eleccion== 3:
    M = (num1 * num2)
    print(f"El resultado es {M}")
elif eleccion == 4:
    D = (num1 / num2)
    print(f"El resultado es {D}")
elif eleccion == 5:
    E = (num1 ** num2)
    print(f"El resultado es {E}")



