Algoritmo Palabra_mas_larga
	Definir p1,p2 Como Caracter;
	Definir diferencia Como Entero;
	Escribir "Ingrese una palabra: ";
	Leer p1;
	Escribir "Ingrese otra palabra: ";
	Leer p2;
	
	diferencia := Abs(Longitud(p1) - Longitud(p2));
	Si Longitud(p1) > Longitud(p2);
		Escribir "La palabra mas larga es ",p1;
	SiNo;
		Escribir "La palabras mas larga es ",p2;
	FinSi
	
	Si Longitud(p1) == Longitud(p2);
		mensaje <- "Las dos palabras tienen el mismo largo";
	FinSi
	
FinAlgoritmo
