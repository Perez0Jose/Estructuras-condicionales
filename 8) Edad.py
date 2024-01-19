#Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:

import datetime

fecha = input("Introduzca su fecha de nacimiento (YYYY-MM-DD):")
fecha =datetime.datetime.strptime(fecha, "%Y-%m-%d")
edad = datetime.datetime.now().year - fecha.year

print("Tu edad es:", edad)












