# =======================================
# Arquivo:      ppt.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:        Otávio Rodrigues Conrado
# Data:         2026.08.04
# Conceitos:    ...
# =======================================

# Importa função randint da biblioteca random, que sorteia um número inteiro aleatório em um intervalo definido
from random import randint

# Importa as funções titulo e linha do arquivo telas,py
from telas import titulo, linha 

# Importa função ler_opcao que valida a entrada do usuário do arquivo modulos.py
from modulos import ler_opcao

# Lista com PEDRA == 0, PAPEL == 1, TESOURA == 2
JOGADAS = ["PEDRA", "PAPEL", "TESOURA"]

# Define o ganhador
def quem_vence(jogador, computador):
    if jogador == computador:
        return "empate"
    if jogador == (computador + 1) % 3:
        return "jogador"
    return "computador"

def mostrar_jogadas():
    print("[0] Pedra")
    print("[1] Papel")
    print("[2] Tesoura")

def jogar_ppt():
    titulo("PEDRA - PAPEL - TESOURA")

    pontos_jogador = 0
    pontos_computador = 0

    while pontos_jogador < 2 and pontos_computador < 2:
        mostrar_jogadas()

        jogador = int(ler_opcao("Sua jogada", ["0", "1", "2"]))
        computador = randint(0, 2)

        print("Você jogou" + JOGADAS[jogador] + ".")
        print("Computador Jogou" + JOGADAS[computador] + ".")

        resultado = quem_vence(jogador, computador)

        if resultado == "empate":
            print("Empate! Ninguém venceu!")
        elif resultado == "jogador":
            pontos_jogador += 1
            print("Você venceu essa rodada!")
        elif resultado == "computador":
            pontos_computador += 1
            print("Computador venceu esta rodada!")

        linha()
        print(f"Placar: Jogador {pontos_jogador} X {pontos_computador} Computador")
        linha()

    if pontos_jogador > pontos_computador:
        titulo("Você ganhou da máquina!")
    else:
        titulo("Você perdeu para a maquina cara")
