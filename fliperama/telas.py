# =======================================
# Arquivo:      telas.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:        Otávio Rodrigues Conrado
# Data:         2026.08.04
# Conceitos:    ...
# =======================================

# Definição da moldura Caracteres e Tamanho
CAR = "="
TAM = 40

# Função para Desenhar uma linha na tela
def linha():
    print(CAR * TAM)

# Função para Desenhar um texto entre linhas
def titulo(texto):
    linha()
    print(texto.center(TAM))
    linha()
