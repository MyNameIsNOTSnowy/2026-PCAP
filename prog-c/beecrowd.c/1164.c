/*
 * Disciplina: 2026-PCAP
 * Problema  : becrowd 1164 - 
 * Autor     : Otávio Conrado
 * Data      : 2026.10.14
*/   
#include <stdio.h>

int eh_perfeito(int n) {
    int i, soma = 0;

    for (i = 1; i < n; i++) {
        if (n % i == 0) {
            soma = soma + i;
        }
    }
    return soma == n;

}

int main() {
    int casos, k, x;

    scanf("%d", &casos);

    for (k = 0; k < casos; k++) {
        scanf("%d", &x);
        if (eh_perfeito(x)) {
            printf("%d eh perfeito\n", x);
        } else {
            printf("%d nao eh perfeito\n", x);
        }
    }

    return 0;
}