/*
Problema:   1073 BeeCrowd
Data:       2026.10.14
Autor:      Otávio Conrado
*/

#include <stdio.h>

int main() {
    int n, i;

    scanf("%d", &n);

    for (i = 2; i <= n; i = i + 2) {
        printf("%d^2 = %d\n", i, i * i);
    }

    return 0;
}   