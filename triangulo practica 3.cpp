#include <iostream>
#include <cstdio>

// Funci�n para calcular el �rea de un tri�ngulo
float calcularArea(float base, float altura) 
{
    return (base * altura) / 2;
}

int main() 
{
    float base, altura, area;

    printf("Programa para calcular el area de un triangulo\n");
    // Solicitar base y altura al usuario
    printf("Ingrese la base del triangulo: ");
    scanf("%f", &base);
    printf("Ingrese la altura del triangulo: ");
    scanf("%f", &altura);

    // base y altura sean positivos
    if (base > 0 && altura > 0) 
	{
        area = calcularArea(base, altura);
        printf("El area del triangulo es: %.2f\n", area);
    } 
	else 
	{
        printf("Error: La base y la altura deben ser valores positivos no negativos.\n");
    }

    return 0;
}

