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

NOMES_DOS_JOGOS = ["Adivinhe o número", "Pedra Papel Tesoura", "Par ou Impar"]
vezes_jogado = [0, 0, 0]

def mostrar_placar():
    titulo("PLACAR")
    for i in range(3):
        print(NOMES_DOS_JOGOS[i] + ": " + str(vezes_jogado[i]) + "x")


NOME_DO_DONO = "Otávio"
OPCOES = ["0", "1", "2", "3"]

while True:

    titulo("FLIPERAMA DO " + NOME_DO_DONO)
    print("[1] Adivinhe o Número")
    print("[2] Pedra Papel Tesoura")
    print("[3] Par ou Ímpar")
    print("[0] Sair")
    linha()
    opcao = ler_opcao("Sua escolha", OPCOES)

    if opcao == "0":
        mostrar_placar()
        titulo("Até a próxima!")
        break
    elif opcao == "1":
        jogar_adivinhe()
    elif opcao == "2":
        jogar_ppt()

