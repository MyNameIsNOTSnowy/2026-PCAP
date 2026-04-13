'''
Problema: beecrowd | 1002
Data: 2026.04.13
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: calcular a área de uma circunferência: area = π . raio2, considerando para este problema que π = 3.14159:

# --- ANÁLISE (LIAC) ---
# Entrada: um número de ponto flutuante
# Processamento: aplicar a fórmula da área se um círculo
# Saída: exibir no formato "A=área"

# float(input()) -> converte o valor lido em decimal
R = float(input())

# o enunciado diz que pi = 3.14159
pi = 3.14159

# R**2 -> raio elevado a segunda potência (R²)
A = pi * (R ** 2)

# :.4f -> formata o número com exatamente 4 casas decimais
print(f"A={A:.4f}")