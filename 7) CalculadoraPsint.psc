Algoritmo CalculadoraPsint
	Definir num1,num2,op,S,R,M,D,E Como Real;
	Definir eleccion Como Entero;
	Escribir "Ingrese un numero: " ;
	Leer num1;
	Escribir "Ingrese otro numero; ";
	Leer num2;
	Escribir "Ingrese un op: 1)Suma  2) Resta 3) Multiplicacion 4) Division 5) Exponenciancion ";
	Leer eleccion;
	
	Si eleccion ==1;
		S <- num1 + num2;
		Escribir "El resultado es: ", S;
	FinSi
	Si eleccion ==2;
		R <- num1-num2;
		Escribir "El resultado es: ", R;
	FinSi
    Si eleccion ==3;
		M <- num1*num2;
		Escribir "El resultado es: ", M;
	FinSi
	Si eleccion ==4;
		D <- num1/num2;
		Escribir "El resultado es: ", D;
	FinSi
	Si eleccion ==5;
		E <- num1^num2;
		Escribir "El resultado es: ", E;
	FinSi

FinAlgoritmo
