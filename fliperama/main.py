# =======================================
# Arquivo:      main.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:        Otávio Rodrigues Conrado
# Data:         2026.08.04
# Conceitos:    ...
# =======================================

# Importar funções de arquivos (módulos)
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from modulos import ler_opcao
from ppt import jogar_ppt
from parouimpar import jogar_POI
from bet import jogar_bet
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores
from placar import salvar_placar, carregar_placar

NOMES_DOS_JOGOS = ["Adivinhe o número", "Pedra Papel Tesoura", "Par ou Impar"]
vezes_jogado = carregar_placar()

def mostrar_placar():
    titulo("PLACAR")
    for i in range(3):
        print(NOMES_DOS_JOGOS[i] + ": " + str(vezes_jogado[i]) + "x")

NOME_DO_DONO = "Otávio"
OPCOES = ["0", "1", "2", "3", "4", "5"]

while True:

    titulo("FLIPERAMA DO " + NOME_DO_DONO)
    print("[1] Adivinhe o Número")
    print("[2] Pedra Papel Tesoura")
    print("[3] Par ou Ímpar")
    print("[4] Cassaníquel")
    print("[0] Sair")
    linha()
    opcao = ler_opcao("Sua escolha", OPCOES)

    if opcao == "0":
        mostrar_placar()
        salvar_placar(vezes_jogado)
        titulo("Até a próxima!")
        break
    elif opcao == "1":
        jogar_adivinhe()
    elif opcao == "2":
        jogar_ppt()
    elif opcao == "3":
        jogar_POI()
    elif opcao == "4":
        jogar_bet()