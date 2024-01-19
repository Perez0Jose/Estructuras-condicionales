#Cuando la Tierra completa una órbita alrededor del Sol, no han transcurrido exactamente 365 rotaciones sobre sí misma, sino un poco más. Más precisamente, la diferencia es de más o menos un cuarto de día.
#Para evitar que las estaciones se desfasen con el calendario, el calendario juliano introdujo la regla de introducir un día adicional en los años divisibles por 4 (llamados bisiestos), para tomar en consideración los cuatro cuartos de día acumulados.
#Sin embargo, bajo esta regla sigue habiendo un desfase, que es de aproximadamente 3/400 de día.
#Para corregir este desfase, en el año 1582 el papa Gregorio XIII introdujo un nuevo calendario, en el que el último año de cada siglo dejaba de ser bisiesto, a no ser que fuera divisible por 400.
#Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año:
 


año = int(input("Ingrese el año deseado:"))

if año <= 1599:
    if(año%4 == 0):
          print(f"{año} Es un año bisiesto")
    else:
        print(f"{año} No es un año bisiesto") 

else:
    if(año%100 == 0 and año%400 == 0):
         print(f"{año} El año es bisiesto")
    else:
         if(año%4 == 0):
              if(año%100 != 0):
                   print(f"{año} Es bisiesto")
              else:
                   print(f"{año} No es bisiesto")
         else:
              print(f"{año} No es bisiesto")          
                      




