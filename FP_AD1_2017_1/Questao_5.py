'''
================================================================================
== UFF - Universidade Federal Fluminense                                      ==
== Tecnologia em Sistemas de Computação                                       ==
== Sérgio Luís de Oliveira Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1                             ==
================================================================================
AD1 - QUESTÃO 5 - Não resolvida!
'''

# Subprogramas

def leMapa(valores, l, c):
    for i in range(l):
        linha = str(input())
        linhaFatiada = []
        for j in range(c):
            linhaFatiada.append(linha[j])
        valores.append(linhaFatiada)
    return


def imprimeMapa(valores):
    for i in range(len(valores)):
        for j in range(len(valores[i])):
            print(valores[i][j], end="")
        print()
    print()
    return


def verificaMapa(valores, posBaseInicialFuncao, i, j):
    if posBaseInicialFuncao == ">":
        if j < (len(valores[i])-1):
            if (valores[i][j+1] == "."):
                verificaMapa(valores, posBaseInicialFuncao, i, j+1)
        else:
            posBaseFinalFuncao = valores[i][j]
            return posBaseFinalFuncao


# Programa Principal

x, y = input().split(" ")
x = int(x)
y = int(y)
mapa = []

leMapa(mapa, x, y)
imprimeMapa(mapa)

posInicioMapa = mapa[0][0]

posBaseInicial = posInicioMapa
nPosBaseInicial = 0
mPosBaseFinal = 0
statusVerificacao = 0

# posBaseFinal, n, m = verificaMapa(mapa, posInicioMapa, 0, 0)
posBaseFinal = verificaMapa(mapa, posInicioMapa, 0, 0)
print(posBaseFinal)
print(n)
print(m)

while statusVerificacao == 0:
    if posBaseInicial == ">":
        if posBaseFinal == "<":
            statusVerificacao = 1
            print("Esse mapa não leva a lugar algum") # - entrei em loop
        elif (nPosBaseInicial == n) and (posBaseFinal == ".") and (y == len(mapa[n])-1):
            statusVerificacao = 1
            print("Esse mapa não leva a lugar algum") # - estourei
        elif (n == 0) and (m == 0):
            statusVerificacao = 1
            print("Esse mapa não leva a lugar algum") # - entrei em círculo
        elif posBaseFinal == "*":
            statusVerificacao = 1
            print("Esse mapa leva ao tesouro")
        elif (posBaseFinal == "<") or (posBaseFinal == "v") or (posBaseFinal == "^"):
            statusVerificacao = 0
            posBaseFinal, n, m = verificaMapa(mapa, posBaseInicial, n, m)

# ============================================================================ #
