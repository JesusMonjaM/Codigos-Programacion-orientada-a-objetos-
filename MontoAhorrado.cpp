#include <iostream>
#include <iomanip>
//Jesus monjaras moreno
//30/05/2025
using namespace std;

class Ahorro
 {
public:
    static void calcularMontoAhorrado() 
	{
        // Datos iniciales
        double depositoMensual = 1000.0;
        double tasaInteresMensual = 0.03; // 3% de interés mensual
        int anios = 10;
        int totalMeses = anios * 12;

        // Variable para guardar el total ahorrado
        double montoAhorrado = 0.0;

        // Algoritmo de monto mensual
        for (int mes = 1; mes <= totalMeses; ++mes) 
		{
            montoAhorrado *= (1 + tasaInteresMensual); // intereses
            montoAhorrado += depositoMensual; // depósito mensual
        }

        // Mostrar el resultado final
        cout << fixed << setprecision(2);
        cout << "Monto ahorrado después de " << anios << " años: $" << montoAhorrado << endl;
    }
};

int main() 
{
    Ahorro::calcularMontoAhorrado();
    return 0;
}

