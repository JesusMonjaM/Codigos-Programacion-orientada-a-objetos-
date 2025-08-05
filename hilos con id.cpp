#include <iostream>
#include <thread>
using namespace std;

void mostrarID(int id) {
    cout << "Hilo número: " << id << endl;
}

int main() {
    thread h1(mostrarID, 1);
    thread h2(mostrarID, 2);
    h1.join();
    h2.join();
    return 0;
}