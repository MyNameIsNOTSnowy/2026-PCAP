'''
Problema: beecrowd | 1009
Data: 2026.04.09
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: Ler nome, salário fixo e total de vendas; calcular e eibir o total a receber

# --- ANÁLISE (LIAC) ---
# Entrada: nome (texto), salário ixo (float), total de vendas efetuadas (float)
# Processamento: comissão = vendas * 0.15 -> total = salário fixo + comissão
# Saída: exibir no formato exato "TOTAL = R$ valor" com 2 casas decimais

# inut() sem conversão -> retorna o nome como texto (str)
n = input()

# float(input()) -> lê valores monetários (podem ter casas decimais)
s = float(input())
v = float(input())

# O vendedor ganha 15% de comissão sobre o total de vendas
c = v * 0.15

# Total a receber = sálario fixo + comissão
st = s + c

# :.2f dentro da f-string -> formata o número com exatamente 2 casas decimais
print(f"TOTAL = R$ {st:.2f}")