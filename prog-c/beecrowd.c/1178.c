/*
 * Disciplina: 2026-PCAP
 * Problema  : becrowd 1178 - Array Fill III
 * Autor     : Otávio Conrado
 * Data      : 2026.10.14
*/   

#include <stdio.h>

int main() {
    double n[100];
    int i;

    scanf("%lf", &n[0]);

    for (i = 1; i < 100; i++) {
        n[i] = n[i - 1] / 2;
    }

    for (i = 0; i < 100; i++) {
        printf("N[%d] = %.4lf\n", i, n[i]);
    }

    return 0;
}