'''
Problema: beecrowd | 1005
Data: 2026.04.13
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: Ler Três notas com pesos diferentes e calcular a média ponderada

# --- ANÁLISE (LIAC) ---
# Entrada: Três notas de ponto flutuante A, B e C
# Processamento: média = (A * 2 + B * 3 + C * 5) / 10
# Saída: Exibir no formato exato "MEDIA = valor" com 1 casa decimal

# float(input()) -> notas podem ter casas decimais
A = float(input())
B = float(input())
C = float(input())

# Nota A tem peso 2, nota B tem peso 3 e nota C tem peso 5
# A soma dos pesos é 10 - divide-se por 10 para descobrir a média ponderada
media = (A * 2 + B * 3 + C * 5) / 10

# :.1f dentro da f-string -> formata o npumero com exatamente 1 casa decimal
print(f"MEDIA = {media:.1f}")