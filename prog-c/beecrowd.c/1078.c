/*
* Disciplina  : 2026-PCAP
* Problema    : beecrowd 1178 - Array Replacement I
* Autor       : Otávio Rodrigues Conrado
* Data        : 2026.10.06
*/

#include <stdio.h>

int main() {
    int n, i;

    scanf("%d", &n);
    for (i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", i, n, i * n);
    }

    return 0;
}