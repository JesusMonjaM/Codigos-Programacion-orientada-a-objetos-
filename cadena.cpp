#include <iostream>
#include <stdio.h>
//Jesus Monjaras Moreno
//26/05/2025
//Sexta practica

int Cadena(const char* cadena) 
{
    char estado = '1';
    for (int i = 0; cadena[i] != '\0'; ++i)
	 {
        char c = cadena[i];
        switch (estado) 
		{
            case '1':
                if (c == 'a') estado = '2';
                break;
            case '2':
                if (c == 'a') estado = '2';
                else if (c == 'b') estado = '3';
                else if (c == 'c') estado = '4';
                else estado = '1';
                break;
            case '3':
                if (c == 'b') estado = '4';
                else if (c == 'a') estado = '1';
                else estado = '1';
                break;
            case '4':
                if (c == 'd') estado = '3';
                else estado = '1';
                break;
        }
    }
    return estado == '4';
}

void procesarCadenaIndividual(const char* cadena) {
    printf("Cadena: %s\n", cadena);
    printf("Resultado: %s\n\n", Cadena(cadena) ? "ACEPTADO" : "NO ACEPTADO");
}

int main() {
    procesarCadenaIndividual("aac");
    procesarCadenaIndividual("cd");
    procesarCadenaIndividual("dcabc");
    procesarCadenaIndividual("kxzz9#a");
    procesarCadenaIndividual("acbdbdcaabaaa");
    return 0;
}

