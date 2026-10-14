/*
Problema:   1113 BeeCrowd
Data:       2026.10.14
Autor:      Otávio Conrado
*/

#include <stdio.h>

int main() {
    int x, y;

    scanf("%d %d", &x, &y);

    while (x != y) {
        if (x < y) {
            printf("Crescente\n");
        } else {
            printf("Decrescente\n");
        }
    
        scanf("%d %d", &x, &y);
    }   

    return 0;
}