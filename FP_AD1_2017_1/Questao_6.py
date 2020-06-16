'''
================================================================================
== UFF - Universidade Federal Fluminense                                      ==
== Tecnologia em Sistemas de Computação                                       ==
== Sérgio Luís de Oliveira Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1                             ==
================================================================================
AD1 - QUESTÃO 6
'''

# Subprogramas

def leAmbiente(valores, l, c):
    for i in range(l):
        linha = str(input())
        linhaFatiada = []
        for j in range(c):
            linhaFatiada.append(linha[j])
        valores.append(linhaFatiada)
    return

def imprimeAmbiente(valores):
    for i in range(len(valores)):
        for j in range(len(valores[i])):
            print(valores[i][j], end="")
        print()
    print()
    return

def analisaAmbiente(valores, x, y):
    # analisa o item da DIREITA
    if y < (len(valores[x])-1):
        if (valores[x][y] == "I") and (valores[x][y+1] == "F"):
            valores[x][y+1] = "I"
            analisaAmbiente(valores, x, y+1)
    # analisa o item da ESQUERDA
    if y > 0:
        if (valores[x][y] == "I") and (valores[x][y-1] == "F"):
            valores[x][y-1] = "I"
            analisaAmbiente(valores, x, y-1)
    # analisa o item ABAIXO
    if x < (len(valores)-1):
        if (valores[x][y] == "I") and (valores[x+1][y] == "F"):
            valores[x+1][y] = "I"
            analisaAmbiente(valores, x+1, y)
    # analisa o item ACIMA
    if x > 0:
        if (valores[x][y] == "I") and (valores[x-1][y] == "F"):
            valores[x-1][y] = "I"
            analisaAmbiente(valores, x-1, y)
    return


# Programa Principal

n = 1
m = 1

while (n != 0) and (m != 0):
    n, m = input().split(" ")
    n = int(n)
    m = int(m)
    ambiente = []

    leAmbiente(ambiente, n, m)
    imprimeAmbiente(ambiente)
    for i in range(n):
        for j in range(m):
            analisaAmbiente(ambiente, i, j)
    imprimeAmbiente(ambiente)

# ============================================================================ #