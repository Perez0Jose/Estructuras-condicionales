#Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula.

import string
import re

while True:
    T = input("Introdusca un caracter:")


    if len(T)==1:
        if T in string.ascii_uppercase:
         print("\t Es una letra mayuscula")

        elif T in string.ascii_lowercase:
            print("\t Es una letra minuscula")

        elif re.match("[0-9]", T):
            print("\t Es un numero")    
        
        else:
            print("\t No es una letra ni un numero")   
    else:
        print("\t Introduce un solo caracter")

     


        