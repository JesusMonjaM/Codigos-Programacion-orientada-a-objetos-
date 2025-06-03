#include <iostream>
#include <string>
#include <stdio.h>

//Jesus Monjaras Moreno
//20-05-2025
//quinta practica

using namespace std;

class Deporte 
{
protected:
    string nombre;
    int jugadores;
    string tipoBalon;
    string tipoUniforme;

public:
    void setDatos(string n, int j, string b, string u) 
	{
        nombre = n;
        jugadores = j;
        tipoBalon = b;
        tipoUniforme = u;
    }

    void mostrarDatos()
	 {
        printf("Nombre del deporte: %s\n", nombre.c_str());
        printf("Número de jugadores: %d\n", jugadores);
        printf("Tipo de balón: %s\n", tipoBalon.c_str());
        printf("Tipo de uniforme: %s\n", tipoUniforme.c_str());
    }
};

class DeporteConPies : public Deporte 
{
public:
    DeporteConPies() {}
};

class DeporteConManos : public Deporte 
{
public:
    DeporteConManos() {}
};

int main() {
    DeporteConPies futbol;
    futbol.setDatos("Fútbol", 11, "Balón redondo", "Camisa, short y tachones");

    DeporteConManos voleibol;
    voleibol.setDatos("Voleibol", 6, "Balón ligero", "Camisa, short y rodilleras");

    printf("DEPORTE CON LOS PIES\n");
    futbol.mostrarDatos();

    printf("\nDEPORTE CON LAS MANOS\n");
    voleibol.mostrarDatos();

    return 0;
}

