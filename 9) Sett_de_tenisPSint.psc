Algoritmo Sett_de_tenis
	Definir a,b Como Entero;
	Escribir "Ingrese el puntaje del jugador A: ";
	Leer a;
	Escribir "Ingrese el puntaje del jugador B: ";
	Leer b;
	Si a==4 y b==5 o a==5 y b==4;
		Escribir "Aun no termina";
	FinSi
	Si a>=5 y b==7 ;
		Escribir "Gano jugador B";
	FinSi
	Si a==5 y b==6 o a==6 y b==5;
		Escribir"Aun no termina";
	FinSi
	Si a==3 y b==7 o a==7 y b==3;
		Escribir "Invalido";
	FinSi
	Si a<=6 y b<=4;
		Escribir "Gano el jugador A";
	FinSi
	Si a<=4 y b<=6;
		Escribir "Gano jugador B";
	FinSi
	Si a==7 y b==5;
		Escribir "Gano el jugador A";
	FinSi
FinAlgoritmo
