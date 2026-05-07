'''
Problema: beecrowd | 1018 - Cédulas
Data: 2026.04.30
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: Dado um valor em reais, determinar a quantidade mínima de cédulas necessárias para compor esse valor

# --- ANÁLISE (LIAC)  ---
# Entrada: Um valor inteiro representando o montante em reais
# Processamento: Utilizar um algoritimo de divisão sucessiva para determinar a quantidade de cédulas necessárias
# Saída: Imprimir a quantidade de cédulas de cada valor necessário para compor

# int(input()) → lê o valor como texto e converte para inteiro
n = int(input())

print(f"{n}")
 
 # Decomposição dos REAIS em notas - sempre da maior para a menor:
# // é divisão INTEIRA (descarta o decimal) → diz QUANTAS notas daquele valor cabem
# % é o RESTO da divisão → guarda o que sobrou para a próxima troca

n100 = n // 100; n = n % 100   # quantas notas de 100 cabem; n vira o resto
n50 = n // 50; n = n % 50      # quantas notas de 50 cabem no que sobrou
n20 = n // 20; n = n % 20      # quantas notas de 20 cabem no que sobrou
n10 = n // 10; n = n % 10      # quantas notas de 10 cabem no que sobrou
n5 = n // 5; n = n % 5         # quantas notas de 5 cabem no que sobrou
n2 = n // 2; n = n % 2         # quantas notas de 2 cabem no que sobrou
n1 = n                        # o que sobrou são notas de 1 real
 
print(f"{n100} nota(s) de R$ 100,00")
print(f"{n50} nota(s) de R$ 50,00")
print(f"{n20} nota(s) de R$ 20,00")
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n2} nota(s) de R$ 2,00")
print(f"{n1} nota(s) de R$ 1,00")