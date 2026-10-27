#include <stdio.h>

int main() {
    char apelido[20];

    scanf("%19s", apelido);

    if (apelido == "sair") {
        printf("igual\n");
    } else {
        printf("diferente\n");
    }

    return 0;
}