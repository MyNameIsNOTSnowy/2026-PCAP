'''
Problema: beecrowd | 1017
Data: 2026.04.23
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: descobrir quantidade de combustível gasto

# --- ANÁLISE (LIAC) ---
# Entrada: Dois números inteiros denominados A e B
# Processamento: Calcular a quantidade de combustível gasto
# Saída: imprimir a quantidade de combustível gasto

A = int(input())
B = int(input())

C = (A * B) / 12
print(f"{C:.3f}")
