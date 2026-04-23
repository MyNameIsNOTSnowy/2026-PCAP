'''
Problema: beecrowd | 1012
Data: 2026.04.23
Estudante: Otávio Rodrigues Conrado
'''
# --- ANÁLISE (LIAC) ---
# Entrada: Três números de ponto flutuante (A, B e C)
# Processamento: Calcular as áreas de um triângulo, círculo, trapézio, quadrado e retângulo
# Saída: Imprimir as áreas calculadas com três casas decimais

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)
pi = 3.14159

triangulo = (A * C) / 2
circulo = pi * (C ** 2)
trapezio = ((A + B) * C) /2
quadrado = B ** 2
retangulo = A * B
print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")