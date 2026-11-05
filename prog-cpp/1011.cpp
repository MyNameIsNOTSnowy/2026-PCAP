/*
 * Disciplina:  2026-PCAP
 * Problema  :  beecrowd 1011 - Esfera
 * Autor     :  Otávio Rodrigues Conrado
 * LIAC      :  calcular e mostrar o volume de uma esfera sendo fornecido o valor de seu raio
 *              A saída deverá ser uma mensagem "VOLUME" com um espaço antes e um espaço depois da igualdade. 
 *              O valor deverá ser apresentado com 3 casas após o ponto.
 */
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int r;
    double volume;

    cin >> r;
    volume = (4 / 3.0) * 3.14159 * r * r * r;
    cout << fixed << setprecision(3);
    cout << "VOLUME = " << volume << endl;

    return 0;

}