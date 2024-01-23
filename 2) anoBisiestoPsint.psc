Proceso anoBisiesto
	Definir ano Como Entero;
	Escribir "Ingrese el año ";
	Leer ano;
	Si (ano <= 1599) Entonces
		Si (ano%4 == 0) Entonces
			Escribir ano, " Es bisiesto ";
		SiNo 
			Escribir ano, " No es bisiesto ";
			
			
		FinSi
	SiNo
		Si (ano MOD 100 == 0 Y ano MOD 400 == 0) Entonces
			Escribir ano, " Es bisiesto ";
		SiNo 
			Si (ano MOD 4 == 0) Entonces
				Si (ano MOD 100 <> 0) Entonces
					Escribir ano, " es bisiesto ";
					
					
				SiNo 
					Escribir ano, " no es bisiesto ";
				FinSi
			SiNo
				Escribir ano, " no es bisiesto ";
			FinSi
		FinSi
	Finsi
FinProceso
