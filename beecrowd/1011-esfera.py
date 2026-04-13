'''
Problema: beecrowd | 1011
Data: 2026.04.13
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: Ler o raio de uma esfera e calcular seu volume com a fórmula (4/3) * pi * R^3

# --- ANÁLISE (LIAC) ---
# Entrada: um número de ponto flutuante (o raio R)
# Processamento: aplicar a fórmula do volume da esfera
# Saída: exibir no formato "VOLUME = valor" com 3 casas decimais

# float() -> converte o valor lido para número decimal (ponto flutuante)
R = float(input())

# o enunciado pede para atribuir pi como constante - não usar math.pi
pi = 3.14159

# 4.0/3 garante divisão decimal (não inteira) - conforme dica do enunciado
# R^3 -> R elevado a terceira potência (R³)
V = (4.0 / 3) * pi * R ** 3

# :.3f -> formata o número com exatamente 3 casas decimais
print(f"VOLUME = {V:.3f}")