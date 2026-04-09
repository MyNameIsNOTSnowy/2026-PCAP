'''
Problema: beecrowd | 1008
Data: 2026.04.09
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: Ler número do funcionario, horas trabalhadas e salario por hora calcular e exibir o total a receber

# --- ANÁLISE (LIAC) ---
# Entrada: número (input), horas trabalhadas (input) e salário por hora (float)
# Processamento: salário = horas trabalhadas * salário por hora
# Saída: exibir no formato exato "NUMBER = "numero do funcionario"" e logo abaixo "SALARY = salário a ser recebido" com 2 casas decimais

# input -> lê o valor fornecido
N = input()

# int(input()) -> lê e converte em uma única instrução
H = int(input())

# float(input()) -> lê valores monetários (podem ter casas decimais)
S = float(input())

# print mostra o que quer que seja colocado entre as "" (use f antes das "" para calculos em geral)
print(f"NUMBER = {N}")
print(f"SALARY = U$ {H*S:.2f}")