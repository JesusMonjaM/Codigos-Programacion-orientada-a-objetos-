#include <iostream>      
#include <fstream>       
#include <vector>        
#include <string>        
//Jesus Monjaras Moreno
//03-06-2025
//decimo primera practica
//codigo que ejecuta un laberinto de 70x70

int main() 
{
    std::ifstream archivo("LaberintoConGuiones.txt");  // Abrir archivo del laberinto
    std::vector<std::string> laberinto;                 // Almacena cada línea del laberinto
    std::string linea;                                  // Variable para leer líneas del archivo

    // Verifica si el archivo se abrió correctamente
    if (!archivo)
	 {
        std::cerr << "No se pudo abrir el archivo 'LaberintoConGuiones.txt'." << std::endl;
        return 1;  // Salir del programa si da error
    }

    // Lee el archivo línea por línea y guardar en el vector
    while (std::getline(archivo, linea)) 
	{
        if (!linea.empty()) 
		{
            laberinto.push_back(linea);  // Es para agrega la línea al vector si no está vacía
        }
    }

    // Muestra el contenido completo del laberinto
    std::cout << "Contenido del laberinto con salida:\n";
    for (size_t i = 0; i < laberinto.size(); ++i)
	 {
        std::cout << laberinto[i] << std::endl;
    }

    // Busca la posición de la salida: primer '-' en la última fila
    const std::string& ultimaFila = laberinto.back();   // Obtiene la última línea
    size_t salida_col = ultimaFila.find('-');           // Busca el primer guion '-'

    // Muestra la posición de la salida si se encuentra
    if (salida_col != std::string::npos) 
	{
        std::cout << "\nSalida encontrada en la fila " << laberinto.size() - 1
                  << " columna " << salida_col << std::endl;
    } 
	else 
	{
        std::cout << "\nNo se encontró salida del laberinto." << std::endl;
    }

    return 0;  
}

