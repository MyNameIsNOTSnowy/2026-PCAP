'''
Problema: beecrowd | 1038
Data: 2026.05.07
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: Ler o código do produto e a quantidade, logo, calcular o valor a ser pago.

# --- ANÁLISE (LIAC) ---
# Entrada: Dois números inteiros, representando o código do produto e, quantidade
# Processamento: Verificar o código do produto, multiplicar a quantidade pelo valor do produto
# Saída: imprimir "Total: R$" seguido do valor a ser pago com exatamente 2 casas decimais

# map(int, input().split()) → Lê uma linha de entrada, divide em partes e converte cada parte para inteiro
A, B = map(int, input().split())

if A == 1:
    total = B * 4.00
elif A == 2:
    total = B * 4.50
elif A == 3:
    total = B * 5.00
elif A == 4:
    total = B * 2.00
else:
    total = B * 1.50
print(f"Total: R$ {total:.2f}")