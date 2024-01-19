#El joven periodista Solarrabietas debe relatar un partido de tenis, pero no conoce las reglas del deporte. En particular, no ha logrado aprender cómo saber si un set ya terminó, y quién lo ganó.
#Un partido de tenis se divide en sets. Para ganar un set, un jugador debe ganar 6 juegos, pero además debe haber ganado por lo menos dos juegos más que su rival. Si el set está empatado a 5 juegos, el ganador es el primero que llegue a 7. Si el set está empatado a 6 juegos, el set se define en un último juego, en cuyo caso el resultado final es 7-6.
#Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le gustaría saber:

    #si A ganó el set, o
    #si B ganó el set, o
    #si el set todavía no termina, o
    #si el resultado es inválido (por ejemplo, 8-6 o 7-3).

#Desarrolle un programa que solucione el problema de Solarrabietas:

a = int(input("Ingrese el puntaje del jugador A: \n"))
b = int(input("Ingrese el puntaje del jugador B: \n"))

if(a == 4 and b == 5) or (a == 5 and b == 4):
    print("Aun no termina")
elif(a >= 5 and b == 7) or (a >= 7 and b == 5):
    print("Gano el jugador B")
elif(a == 5 and b == 6) or (a == 6 and b == 5):
    print("Aun no termina")
elif(a == 3 and b == 7) or (a == 7 and b == 3):
    print("Invalido")
elif(a <= 6 and b <= 4) or (a <= 4 and b <= 6):
    print("Gano el jugador A")












