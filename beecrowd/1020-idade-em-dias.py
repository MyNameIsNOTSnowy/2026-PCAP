'''
Problema: beecrowd | 1020
Data: 2026.04.13
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: Ler um número inteiro D repesentando dias e converter em ano(s) mes(es) e dias restantes

# --- ANÁLISE (LIAC) ---
# Entrada: um número inteiro D representando total de dias sobrevividos
# Processamento: extrair anos, meses e dias totais sobrevividos por divisão inteira e módulo
# Saída: no formato "A ano(s) M mes(es) B dia(s)" com um em cada linha

# int(input()) -> tempo vivo sempre será um número inteiro em dias
D = int(input())

# // -> divisão inteira: retorna quantas vezes o divisor cabe no dividendo
# % -> módulo: retorna apenas o resto da divisão

# Quantos anos completos cabem em D dias? (1 ano = 365 dias)
A = D // 365

# Dias restantes após retirar os anos completos
D = D % 365

# Quantos meses completos cabem nos dias restantes? (1 mes = 30 dias)
M = D // 30

# Dias que sobram após retirar os meses completos
B = D % 30

# print -> ..-. ..- -. -.-. .- --- / . -- -... ..- - .. -.. .- / ..- - .. .-.. .. --.. .- -.. .- / .--. .- .-. .- / . -..- .. -... .. .-. / .. -. ..-. --- .-. -- .- -.-. --- . ... / -.--. - . -..- - --- --..-- / -. ..- -- . .-. --- ... --..-- / .-. . ... ..- .-.. - .- -.. --- ... / -.. . / --- .--. . .-. .- . ... -.--.- / -. --- / -.-. --- -. ... --- .-.. . / --- ..- / - . .-. -- .. -. .- .-.. .-.-.-
print(f"{A} ano(s)")
print(f"{M} mes(es)")
print(f"{B} dia(s)")