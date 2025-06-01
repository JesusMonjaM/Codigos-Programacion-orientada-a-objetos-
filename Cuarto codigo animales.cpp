#include <iostream>
#include <string>
#include <stdio.h>

//Jesus Monjaras Moreno
//15-05-2025
//cuarto programa

using namespace std;

class Animales
 {
protected:
    string color;
    string raza;
    string patas;
    string colas;

public:
    void setDatos(string c, string r, string p, string co)
	 {
        color = c;
        raza = r;
        patas = p;
        colas = co;
    }

    void mostrarDatos() 
	{
        printf("Raza: %s\n", raza.c_str());
        printf("Color: %s\n", color.c_str());
        printf("Patas: %s\n", patas.c_str());
        printf("Colas: %s\n", colas.c_str());
    }
};

class Vertebrado : public Animales 
{
public:
    Vertebrado() {}
};

class Invertebrado : public Animales 
{
public:
    Invertebrado() {}
};

int main() 
{
    Vertebrado gato;
    gato.setDatos("Negro", "Persa", "4", "1");

    Invertebrado mariposa;
    mariposa.setDatos("Amarilla", "Monarca", "6", "0");

    printf("VERTEBRADO\n");
    gato.mostrarDatos();

    printf("\nINVERTEBRADO\n");
    mariposa.mostrarDatos();

    return 0;
}
