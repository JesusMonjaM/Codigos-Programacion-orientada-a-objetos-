#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
//Jesus Monjaras Moreno
//30-05-2025
//quinto programa
int main() 
{
    std::ifstream archivo("HOLA A TODO MUNDO.txt");
    std::stringstream buffer;
    std::string contenido;

    if (archivo) 
	{
        buffer << archivo.rdbuf();
        contenido = buffer.str();

        std::cout << "Este es el contenido del archivo:\n";
        std::cout << contenido << std::endl;
    } 
	else 
	{
        std::cerr << "No se encontro el archivo." << std::endl;
    }

    return 0;
}
