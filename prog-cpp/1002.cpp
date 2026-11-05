/*
 * Disciplina:  2026-PCAP
 * Problema  :  beecrowd 1002 - Area do Circulo
 * Autor     :  Otávio Rodrigues Conrado
 * LIAC      :  Le o raio R (real). Calcula a area com pi = 3.14159 e
 *              imprime "A=area" com quatro casas decimais.
 */
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double r, area;

    cin >> r;
    area = 3.14159 * r * r;
    cout << fixed << setprecision(4);
    cout << "A=" << area << endl;

    return 0;
}