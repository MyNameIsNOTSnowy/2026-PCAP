'''
Problema: beecrowd | 1001
Data: 2026.04.07
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: descrição sucinta do que o programa deve fazer

# --- ANÁLISE (LIAC) ---
# Entrada: dois números inteiros, cada um em uma linha separada
# Processamento: somar A + B e armazenar em X
# Saída: exibir no formato exato "X = valor" (espaços ao redor do =, sem mensagens extras)

# int()   -> converte o texto lido para número inteiro
# input() -> lê o valor ornecido (digitado ou pelo Beecrowd)
# int(input()) -> lê e converte em uma única instrução
A = int(input(""))
B = int(input(""))

# O enunciado especifíca explicitamente as variáveis A, B e X - seguir à risca
X = A + B

# f-string: insere o valor de X dentro do texto com {}
# Atenção: espaço antes e depois do = é obrigatório conforme o enunciado
print(f"X = {A+B}")