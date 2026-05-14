'''
Problema: beecrowd | 1046
Data: 2026.05.14
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar no outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

# --- ANÁLISE (LIAC) ---
# Entrada: ler 2 numeros inteiros denominados A e B
# Processamento: calcular o tempo total do jogo em horas
# Saída: exibir exatamente "O JOGO DUROU *** HORA(S)"

# input().split() → lê 2 números inteiros e os armazena respectivamente em A e B
A, B = input().split()
# int() → converte os valores de A e B para inteiros
A = int(A)
B = int(B)

C = (A * 60)
D = (B * 60)

# if/elif/else → verifica uma série de condições para calcular o tempo total do jogo em horas
if C > D:
    E = (D - C) + (24 * 60)
else:
    E = D - C
if A == B:
    E = 24 * 60

# print() → exibe o que está dentro das ""
print(f"O JOGO DUROU {E // 60} HORA(S)")