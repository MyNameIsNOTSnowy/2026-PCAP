'''
Problema: beecrowd | 1047 - Tempo de Jogo com Minutos
Data: 2026.05.07
Estudate: Otávio Rodrigues Conrado
'''
# Objetivo: Calcular a DURAÇÃO de um jogo (em horas e minutos), sabendo a hora de início (hi:mi) e a hora de fim (hf:mf) . O jogo dura no MÍNIMO 1 minuto e no MÁXIMO 24 horas.

# --- ANÁLISE (LIAC) ---
# Entrada: 4 inteiros na MESMA linha → hi mi hf mf (hora/minuto inicial e final)
# Processamento: converter início de fim para o total em MINUTOS, se o fim for menor ou igual ao início, o jogo "virou a meia-noite". (somar 24h em minutos), converter a duração de volta para horas e minutos
# Saída: "O JOGO DUROU H HORA(S) E M MINUTO(S)"

# input().split() lê a linha e a quebra em pedaços por ESPAÇO
# map(int, ...) aplica int() em CADA pedaço de uma vez 
# Os 4 valores são desempacotados nas 4 variáveis na ordem
hi, mi, hf, mf = map(int, input().split())