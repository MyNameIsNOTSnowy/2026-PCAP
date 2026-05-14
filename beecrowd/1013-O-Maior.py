'''
Problema: beecrowd | 1013
Data: 2026.05.07
Estudante: Otávio Rodrigues Conrado
'''
#Objetivo: Ler 3 valores inteiros e apresentar o maior deles

# --- ANÁLISE (LIAC) ---
# Entrada: 3 valores inteiros
# Processamento: Comparar os 3 valores e determinar o maior
# Saída: O maior valor entre os 3 seguido de "eh o maior"

# int(input()) converte texto em um valor inteiro
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

# Função para encontrar o maior valor entre A, B e C usando ">=" → maior ou igual, e "if/elif/else" para comparar os comandos
if A >= B and A >= C:
    print(f"{A} eh o maior")
elif B >= A and B >= C:
    print(f"{B} eh o maior")
else:
    print(f"{C} eh o maior")
