/*
* Disciplina: 2026-PCAP
* Projeto   : Fliperama em C
* Autor     : Otávio Rodrigues Conrado
* LIAC      : Menu Com validação e blah blah blah
*/

#include <stdio.h>

#define DONO "Otávio.Conrado"

void linha() {
    printf("============================================================\n");
}

void titulo(char texto[]){
    linha();
    printf("    %s\n", texto);
    linha();
}

int ler_numero(char mensagem[], int minimo, int maximo) {
    int numero, lidos;

    printf("    %s:", mensagem);
    lidos = scanf("%d", &numero);
    while (lidos != 1 || numero < minimo || numero > maximo){
        if (lidos != 1){
            scanf("%*s");
        }
        printf("Opcao invalida! Tente de novo: ");
        lidos = scanf("%d", &numero);
    }
    return numero;
}

void mostrar_menu() {
    linha();
    printf("    FFLIPERAMA DO %s\n", DONO);
    linha();
    printf("[1] Adivinhe o Numero\n");
    printf("[2] Cadastra Jogador\n");
    printf("[3] Listar Jogadores\n");
    printf("[0] Sair\n");
    linha();
}



int main() {
    int opcao;

    mostrar_menu();
    opcao = ler_numero("Sua escolha", 0, 3);
    while (opcao != 0){
        if (opcao == 1) {
            printf("O Jogo entra na Fase #.\n");
        }else if (opcao == 2) {
            printf("O cadastro entra na Fase 2.\n");
        }else {
            printf("A lista entra na Fase 2.\n");
        }
        mostrar_menu();
        opcao = ler_numero("Sua escolha", 0, 3);
    }

    titulo("Ate a proxima!");
    return 0;
}