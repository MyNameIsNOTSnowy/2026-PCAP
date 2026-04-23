'''
Problema: beecrowd | 1035
Data: 2026.04.23
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: Ler quatro valores e verificar se eles atendem tais condições

# --- ANÁLISE (LIAC) ---
# Entrada: quatro números inteiros denominados A, B, C e D
# Processamento: verificar se todas as condições são verdadeiras e em seguida mostra tal mensagem
# Saída: mostrar a mensagem "Valores não aceito" se as condições não forem atendidas ou "Valores aceitos" caso contrário

A, B, C, D = input().split()

A = int(A)
B = int(B)
C = int(C)
D = int(D)

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")