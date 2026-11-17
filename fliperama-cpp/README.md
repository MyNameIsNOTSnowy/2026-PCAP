# Fliperama em C++ (MeuApp v4.0)

## O que e
um programa de um fliperama com 1 jogod e adivinhar o numero, e que também é capaz e cadastrar jogadores

## Como compilar e rodar
g++ -Wall fliperama.cpp -o fliperama
./fliperama

## Arquivos
- fliperama.cpp: [O FLIPERAMA EM SI]
- jogadores.csv: [onde fica os jogadorES E SUAS PARTIDAS JOgadas, cada coluna guarda um jogador e numero de partidas]

## C x C++: o que mudou
C: if (strcmp(apelidos[i], procurado) == 0) {
C++: if (apelidos[i] == procurado) {

## O que o C++ decidiu por mim
[duas linhas: uma coisa que em C voce escrevia e em C++ a linguagem faz]

## Autoavaliacao
| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git | C | 9 - 177 |
| 2. Cadastro: vectors e referencia | C | 46 - 108 |
| 3. Jogo e partidas | C | 110 - 139 |
| 4. Persistencia | C | 141 - 150 |
| 5. Documentacao e comparacao | C | 152 - 177 |