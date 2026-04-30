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

n = int(input())
print(f"{n}")
 
n100 = n // 100; n = n % 100
n50 = n // 50; n = n % 50
n20 = n // 20; n = n % 20
n10 = n // 10; n = n % 10
n5 = n // 5; n = n % 5
n2 = n // 2; n = n % 2
n1 = n
 
print(f"{n100} nota(s) de R$ 100,00")
print(f"{n50} nota(s) de R$ 50,00")
print(f"{n20} nota(s) de R$ 20,00")
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n2} nota(s) de R$ 2,00")
print(f"{n1} nota(s) de R$ 1,00")