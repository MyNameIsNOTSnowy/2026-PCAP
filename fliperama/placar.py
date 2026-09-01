# =============================================
# ARQUIVO   : placar.py (pasta fliperama)
# Conceitos : Arquivo de texto, modo de abertura, write, close
# =============================================

ARQUIVO = "placar.csv"
NOMES = ["Adivinhe o Numero", "Pedra-Papel-Tesoura", "Par ou Impar", "Cassaníquel"]


def salvar_placar(vezes):
    # "w" esvazia o arquivo e escreve tudo de novo.
    arquivo = open(ARQUIVO, "w")
    for i in range(3):
        arquivo.write(NOMES[i] + "," + str(vezes[i]) + "\n")
    arquivo.close()

def carregar_placar():
    arquivo = open(ARQUIVO, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    vezes = []
    for linha_lida in linhas:
        pedaços = linha_lida.strip().split(",")
        vezes.appen(int(pedaços[1]))

    return vezes