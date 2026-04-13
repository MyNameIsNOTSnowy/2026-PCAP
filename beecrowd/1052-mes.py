'''
Problema: beecrowd | 1052
Data: 2026.04.13
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: Ler um número inteiro e informar qual mês ele representa

# --- ANÁLISE (LIAC) ---
# Entrada: um número inteiro representado por N
# Processando: comparar o número inteiro com cada mês da lista, exibir "não existe mês (13 - ∞)", caso número seja negativo ou 0 "não existe mês (-∞ - 0)"
# Saída: informe o mês correspondente ao inteiro, se o número não corresponder, exibir "(qualquer número fora da cadeia 1-12) isn't a month KID"

# int(input()) -> Mês sempre será número inteiro
M = int(input())

# estrutura if/elif/else: testa cada condição em sequência
# Apenas o primeiro bloco verdadeiro é executado - os demais são ignorados
if M == 1:
    print("January")
elif M == 2:
    print("February")
elif M == 3:
    print("March")
elif M == 4:
    print("April")
elif M == 5:
    print("May")
elif M == 6:
    print("June")
elif M == 7:
    print("July")
elif M == 8:
    print("August")
elif M == 9:
    print("September")
elif M == 10:
    print("October")
elif M == 11:
    print("November")
elif M == 12:
    print("December")
else:
    print(f"{M} isn't a month KID")