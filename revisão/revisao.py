# mkdir → Cria uma pasta/diretório
# code → cria um arquivo diretório

import random

# Fundamentos da programação:

#   1- Variáveis e tipos de dados.

# Variáveis armazenam dados em geral sendo sempre altomáticamente definidos como palavras
guh = 2

# Os tipos de dados podem variar de textos a números inteiros ou decimais:

# Dado definido como numero inteiro
guh2 = int(1)

# Dado definido como numero decimal
guh3 = float(1.9)
guh4 = 2.9

#   2- Operadores

# Executam uma operação por cima de uma variável e seu valor

# + (adição), - (subtração), * (multiplicação), / (divisão normal), // (divisão inteira), ** (exponenciação). 
guh4 == guh3 + guh2


#   3- Entrada de dados

# Usuário falando com computador/dando informações ao computador

# input() Recebe texto
input("texto: ")

# input() junto de int() define a entrada como número inteiro
int(input("número inteiro: "))

# input() junto de float() define a entrada como número decimal
float(input("número decimal: "))

#   4- Saída de dados

# Computador falando com usuário

# Use print("") para definir uma saída de dados
# Caso seu código contenham operadores e você precise mostrar uma resposta a partir da variável imposta sobre tal use f antes das ""
print(f"Saída: {guh4}")

#   5- Estrutura de Repetição

# Usada para repetir um comando 

# for usado quando se há um limite de repetições
for tempo in range(3):
    print("for: pão")

# while é usado para repetir um código até que outro seja executado
tempo = 0

while tempo <= 2:
    print("while: cheese")
    tempo = tempo + 1

#   6- Estrutura de Condição

# Testa códigos para definir qual "caminho" seguir na sua linha de código
pães = random.randint(1, 2)

# Se pães for 1 ele seguirá o primeiro caminho e printará "👍"
if pães == 1:
    print("if: 👍")

# Se pães for 2 ele seguirá o segundo caminho e printará "👎"
else:
    print("else: 👎")

#   7- Sub-rotinas
