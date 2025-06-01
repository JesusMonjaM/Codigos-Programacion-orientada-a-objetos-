#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

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
