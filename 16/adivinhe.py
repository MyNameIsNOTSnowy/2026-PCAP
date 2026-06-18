# ============================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Adivinhe o Número"
# Arquivo    : adivinhe.py
# Autor      : Otávio Rodrigues Conrado
# Data       : 2026.05.28
# ============================================================

import random

def jogar(maximo, chances):
    numero_secreto = random.randint(1, maximo)
    acertou = False

    while chances > 0 and not acertou:
        palpite = int(input("Seu palpite (1 a " + str(maximo) + ")"))

        if palpite == numero_secreto:
            print("🎉 Acertou!")
            acertou = True
        elif palpite < numero_secreto:
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
    ["Difícil", 1000, 10],
    ["Impossível", 10000, 20],
    ["Sorte Pura 💀", 100000, 1]
]

# === Menu de escolha do nível ===
print("Escolha o nível de dificuldade:")
print("1 - Fácil         (1 a 10, 3 chances)")
print("2 - Médio         (1 a 100, 5 chances)")
print("3 - Difícil       (1 a 1000, 10 chances)")
print("4 - Impossivel    (1 a 10000, 20 chances)")
print("5 - Sorte Pura 💀 (1 a 100000, 1 chance)")
opcao = int(input("Digite 1, 2 ou 3: "))

# A opção 1 está na posição 0 da lista, por isso ajuste
nivel = niveis[opcao - 1]

# === Iniciamos o jogo com a configuração do nível escolhido ===
print("Você escolheu o nível:", nivel[0])
venceu = jogar(nivel[1], nivel[2])

if not venceu:
    print("💀 Fim de jogo Tente um nível mais fácil. 😉")