#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.

p1 = str(input("Ingrese uma palabra: "))
p2 = str(input("Ingrese otra palabras: "))

diferencia = abs((len(p1)) - len(p2))

if len(p1) > len(p2):
    mensaje = f"La palabra {p1} tiene {diferencia} letras más que {p2}."
elif len(p1) < len(p2):
    mensaje = f"La palabra {p2} tiene {diferencia} letras más que {p1}."
else:
    mensaje = "Las dos palabras tienen el mismo largo."

print(mensaje)    
    
    










