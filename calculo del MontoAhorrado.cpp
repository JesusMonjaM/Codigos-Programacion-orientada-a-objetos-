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
        // Datos iniciales solicitados
        double depositoMensual = 15000.0;
        double tasaInteresMensual = 0.037; // 3.7% de interés 
        int anios = 15;
        int totalMeses = anios * 12;

        // Variable para guardar el total 
        double montoAhorrado = 0.0;

        // Algoritmo mensual
        for (int mes = 1; mes <= totalMeses; ++mes) 
		{
            montoAhorrado *= (1 + tasaInteresMensual); // capitalización
            montoAhorrado += depositoMensual; // depósito mensual
        }

        // Mostrar el resultado 
        cout << fixed << setprecision(2);
        cout << "Monto ahorrado después de " << anios << " años: $" << montoAhorrado << endl;
    }
};
int main()
 {
    Ahorro::calcularMontoAhorrado();
    return 0;
}
