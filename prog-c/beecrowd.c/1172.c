/*
* Disciplina  : 2026-PCAP
* Problema    : beecrowd 1172 - Array Replacement I
* Autor       : Otávio Rodrigues Conrado
* Data        : 2026.10.06
* LIAC        : ler 10 numeros inteiros num vetor x. Troca os valor menores ou iguais a 0 por 1. Imprime cada posicao
*/

#include <stdio.h>

int main() {
    int x[10], i;

    for (i = 0; i <10; i++) {
        scanf("%d", &x[i]);
        if (x[i] <= 0) {
            x[i] = 1;
        }
    }

    for (i = 0; i < 10; i++) {
        printf("X[%d] = %d\n", i, x[i]);
    }

    return 0;
}