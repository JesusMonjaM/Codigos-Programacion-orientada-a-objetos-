#include <iostream>
#include <thread>
using namespace std;

void hola() {
    cout << "Hola desde el hilo\n";
}

int main() {
    thread hilo1(hola);  // Crea el hilo
    hilo1.join();        // Esperar a que termine el hilo
    cout << "Fin del programa\n";
    return 0;
} 