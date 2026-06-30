# ============================================================
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Par ou Ímpar"
# Arquivo    : par_impar.py
# Autor      : Otávio Rodrigues Conrado
# Data       : 2026.06.25
# ============================================================
import random

opcoes = ["par", "impar", "ímpar"]

jogada = input("Escolha impar ou par: ").lower().strip()

if jogada in opcoes:
    Njogada = int(input(f"Você escolheu {jogada}, escolha um número de 0 a 5: "))

numero_secreto = random.randint(1, 2)

if (Njogada + numero_secreto) % 2 == 1 and jogada == "par":
    print("Você perdeu! haha")
elif (Njogada + numero_secreto) % 2 == 1 and jogada != "par":
    print("Você ganhou eu acho...")
elif (Njogada + numero_secreto) % 2 == 0 and jogada != "par":
    print("Você perdeu! haha")
else:
    print("Você ganhou eu acho")

S = (Njogada + numero_secreto)

if S % 2 == 1:
    P = "impar"
else:
    P = "par"

print(f"{Njogada} + {numero_secreto} = {S}, e {S} é {P}")