#Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los lados no puede ser más largo que la suma de los otros dos.
#Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:

    #si acaso el triángulo es inválido; y
    #si no lo es, qué tipo de triángulo es.

l1 = float(input("Ingrese el primer numero:"))
l2 = float(input("Ingrese el segundo numero:"))
l3 = float(input("Ingrese el tercer numero:"))

if (l1 == l2 != l3):
    print("El triangulo es isoceles")
elif (l1 != l2 != l3): 
    print("El triangulo es escaleno")  
else:
    print("Es triangulo es invalido")





