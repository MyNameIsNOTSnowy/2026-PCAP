# Fliperama em C (MeuApp v3.0)

## O que e
é um fliperama jogavel com cadastro de jogadores feito na linguagem de programação C

## Como compilar e rodar
gcc -Wall fliperama.c -o fliperama
./fliperama

## Arquivo
- fliperama.c: [uma linha]
- jogadores.csv: [uma linha: o que cada coluna guarda]

## Python x C: o que mudou
No Python a maioria dos codigos já decidiam uma ação sozinhos coisa que no C você tem de escrever manualmente como %s, %d e o símbolo &

## O que o C me obrigou a decidir
Uso obrigatório de formatadores como %s (string/texto) e %d (inteiro), além do símbolo & para indicar o endereço de memória.

## Autoavaliacao
| Criterio | B | fliperama.c (9 - 179) |
|---|---|---|
| 1. Estrutura, compilacao e Git | B | A estrutura foi seguida corretamente |
| 2. Cadastro: menu, funcoes e vetores | B | linhas 9 - 87 |
| 3. Jogo e partidas | B | linhas 89 - 179 |
| 4. Persistencia | B | linhas 119 - 141 |
| 5. Documentacao e comparacao | B | Documentação [README.md] |