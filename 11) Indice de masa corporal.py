#El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal:

 	#edad < 45	edad ≥ 45
#IMC < 22.0	bajo	medio
#IMC ≥ 22.0	medio	alto
#El índice de masa corporal es el cuociente entre el peso del individuo en kilos y el cuadrado de su estatura en metros.

#Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.

import math
imc = float(input("Ingrese su peso: \n")) / (math.pow(float(input("Ingrese su altura")),2))
edad = int(input("Ingrese su edad: \n"))

if edad < 45 and imc < 22.0:
    print("Bajo")
elif edad >= 45 and imc < 22.0:
    print("medio")
elif edad < 45 and imc >= 22.0:
    print("medio")
else :
    print("Alto")




















