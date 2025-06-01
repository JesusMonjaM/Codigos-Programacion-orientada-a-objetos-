#include <iostream>
#include <cstdio>
#define PI 3.1416

class Circulo //circulo con clases  Practica 2 jesus monjaras moreno
 {
private:
    float radio;
    char medida[10];
    int opcion;

public:
    void ejecutar() 
	{
        printf("¿Qué deseas calcular?\n");
        printf("1. Area\n");
        printf("2. Perimetro\n");
        printf("Ingresa tu opcion (1 o 2): ");
        scanf("%d", &opcion);

        printf("\nIngresa el radio del circulo: ");
        scanf("%f", &radio);

        printf("Ingresa la unidad de la medida. cm, m: ");
        scanf("%s", medida);

        if (opcion == 1)
		 {
            float area = PI * radio * radio;
            printf("\nEl area es: %.2f %s^2\n", area, medida);
        } 
		else if (opcion == 2) 
		{
            float perimetro = 2 * PI * radio;
            printf("\nEl perimetro es: %.2f %s\n", perimetro, medida);
        }
		 else
		 {
            printf("\nOpcion invalida.\n");
        }
    }
};

int main()
 {
    Circulo c;
    c.ejecutar();
    return 0;
}
