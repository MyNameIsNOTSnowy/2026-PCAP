/*
 * Disciplina: 2026-PCAP
 * Problema  : becrowd 1180 - Menor e Posição
 * Autor     : Otávio Conrado
 * Data      : 2026.10.14
*/   
#include <stdio.h>

int posicao_do_menor(int v[], int n) {
    int i, pos = 0;

    for (i = 1; i < n; i++) {
        if (v[i] < v[pos]) {
            pos = i;
        }
    }

    return pos;
}

int main() {
    int v[1000], n, i, pos;

    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    pos = posicao_do_menor(v, n);

    printf("Menor valor: %d\n", v[pos]);
    printf("Posicao: %d\n", pos);

    return 0;
}