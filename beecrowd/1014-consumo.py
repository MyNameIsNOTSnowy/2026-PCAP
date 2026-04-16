'''
Problema: beecrowd | 1014
Data: 2026.04.16
Estudante: Otávio Rodrigues Conrado
'''
# Objetivo: Calcular o consumo médio de um automóvel em km/l

# --- ANÁLISE (LIAC) ---
# Entrada: _____________ (inteiro, em km) e _____________ (float, em litros)
# Processamento: consumo = _____ / _____
# Saída: consumo com _____ casas decimais seguido de "___________"

# Lê a distância total percorrida em km (tipo inteiro)
X = int(input())

# Lê o total de combustível gasto em litros (tipo ponto flutuante)
Y = float(input())

# Calcula o consumo médio: quilômetros dividido por litros
consumo = X / Y

# Exibe o resultado com 3 casas decimais e unidade km/l
print(f"{consumo:.3f} km/l")