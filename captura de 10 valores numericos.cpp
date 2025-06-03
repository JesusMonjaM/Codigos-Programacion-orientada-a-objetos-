#include <iostream>
#include <algorithm>

//Jesus Monjaras Moreno
//28/05/2025
//septima  practica

using namespace std;

int main() 
{
    int numeros[10];

    //Pide 10 números
    for (int i = 0; i < 10; i++)
	 {
        cout << "Ingresa el numero: ";
        cin >> numeros[i];
    }

    //Ordena de menor a mayor a manera de (burbuja)
    for (int i = 0; i < 9; i++)
	 {
	 	
        for (int j = i + 1; j < 10; j++) 
		{
            if (numeros[i] > numeros[j]) 
			{
                int temp = numeros[i];
                numeros[i] = numeros[j];
                numeros[j] = temp;
            }
        }
    }

    //Muestra los números de manera ordenada
    cout << "\nNumeros ordenados:\n";
    for (int i = 0; i < 10; i++) 
	{
        cout << numeros[i] << " ";
    }
    cout << endl;

    return 0;
}


