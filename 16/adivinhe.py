# ============================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Adivinhe o Número"
# Arquivo    : adivinhe.py
# Autor      : Otávio Rodrigues Conrado
# Data       : 2026.05.28
# ============================================================

import random

def jogar(maximo, chances):
    numero_secreto = random.randit(1, maximo)
    acertou = False

    while chances > 0 and not acertou:
        palpite = int(input("Seu palpite (1 a " + str(maximo) + ")"))

        if palpite == numero_secreto:
            print("🎉 Acertou!")
            acertou = True
        elif palpite > numero_secreto:
            print("📈 Muito baixo!")
        else:
            print("📉 Muito alto!")

        chances = chances - 1
        print ("Chances restantes:", chances)

    return acertou

# === Níveis guardados em uma lista de listas: [nome, maximo, chances] ===
niveis = [
    ["Fácil", 10, 3],
    ["Médio", 100, 5],
    ["Impossível", 1000, 10],
]

# === Menu de escolha do nível ===