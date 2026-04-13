'''
Problema: beecrowd | 1050
Data: 2026.04.13
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: Ler um codigo DDD e informar a que cidade ele pertence

# --- ANÁLISE (LIAC) ---
# Entrada: um número inteiro representando código DDD
# Processamento: comparar o  DDD lido com cada código da tabela usando if/elif/else
# Saída: nome da cidade correspondente, ou "DDD não cadastrado" se não encontrado

# int(input()) -> DDD sempre será um número inteiro
DDD = int(input())

# Estrutura if/elif/else: testa cada condição em sequência
# Apenas o primeiro bloco verdadeiro é executado os demais são ignorados
if DDD == 61:
    print("Brasília")
elif DDD == 71:
    print("Salvador")
elif DDD == 11:
    print("São Paulo")
elif DDD == 21:
    print("Rio de Janeiro")
elif DDD == 32:
    print("Juíz de fora")
elif DDD == 19:
    print("Campinas")
elif DDD == 27:
    print("Vitória")
elif DDD == 31:
    print("Belo Horizonte")
else:
    # Nenhuma condição acima foi verdadeira -> DDD não está na tabela
    print("DDD Não cadastrado")