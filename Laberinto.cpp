#include <iostream>      // Para entrada y salida est�ndar
#include <fstream>       // Para manejo de archivos
#include <vector>        // Para almacenar el laberinto en una matriz
#include <string>        // Para manejar texto l�nea por l�nea
//Jesus Monjaras Moreno
//03-06-2025
//decimo primera practica

int main() 
{
    std::ifstream archivo("LaberintoConGuiones.txt");  // Abrir archivo del laberinto
    std::vector<std::string> laberinto;                 // Almacena cada l�nea del laberinto
    std::string linea;                                  // Variable para leer l�neas del archivo

    // Verifica si el archivo se abri� correctamente
    if (!archivo)
	 {
        std::cerr << "No se pudo abrir el archivo 'LaberintoConGuiones.txt'." << std::endl;
        return 1;  // Salir del programa si da error
    }

    // Lee el archivo l�nea por l�nea y guardar en el vector
    while (std::getline(archivo, linea)) 
	{
        if (!linea.empty()) 
		{
            laberinto.push_back(linea);  // Es para agrega la l�nea al vector si no est� vac�a
        }
    }

    // Muestra el contenido completo del laberinto
    std::cout << "Contenido del laberinto con salida:\n";
    for (size_t i = 0; i < laberinto.size(); ++i)
	 {
        std::cout << laberinto[i] << std::endl;
    }

    // Busca la posici�n de la salida: primer '-' en la �ltima fila
    const std::string& ultimaFila = laberinto.back();   // Obtiene la �ltima l�nea
    size_t salida_col = ultimaFila.find('-');           // Busca el primer guion '-'

    // Muestra la posici�n de la salida si se encuentra
    if (salida_col != std::string::npos) 
	{
        std::cout << "\nSalida encontrada en la fila " << laberinto.size() - 1
                  << " columna " << salida_col << std::endl;
    } 
	else 
	{
        std::cout << "\nNo se encontr� salida del laberinto." << std::endl;
    }

    return 0;  
}

