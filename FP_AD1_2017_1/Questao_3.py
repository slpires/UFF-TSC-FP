'''
================================================================================
== UFF - Universidade Federal Fluminense                                      ==
== Tecnologia em Sistemas de Computação                                       ==
== Sérgio Luís de Oliveira Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1                             ==
================================================================================
AD1 - QUESTÃO 3
'''

import random

# Subprogramas

def geraMatriz(valores, l, c):
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(random.randint(10,99))
        valores.append(linha)
    return

def imprimeMatriz(valores):
    for i in range(len(valores)):
        for j in range(len(valores[i])):
            print(valores[i][j], end=" ")
        print()
    print()
    return

def identificaSubMatriz(valores):
    if (len(valores) >= 3) and (len(valores[0]) >= 3):
        for i in range(1,len(valores)-1):
            for j in range(1,len(valores[i])-1):
                if (valores[i][j] < valores[i-1][j-1]) and \
                   (valores[i][j] < valores[i-1][j])   and \
                   (valores[i][j] < valores[i-1][j+1]) and \
                   (valores[i][j] < valores[i+1][j-1]) and \
                   (valores[i][j] < valores[i+1][j])   and \
                   (valores[i][j] < valores[i+1][j+1]) and \
                   (valores[i][j] < valores[i][j-1])   and \
                   (valores[i][j] < valores[i][j+1]):
                        print("%d %d %d" %(valores[i-1][j-1], valores[i-1][j], valores[i-1][j+1]))
                        print("%d %d %d" %(valores[i][j-1], valores[i][j], valores[i][j+1]))
                        print("%d %d %d" %(valores[i+1][j-1], valores[i+1][j], valores[i+1][j+1]))
                        print()
    return


# Programa Principal

l, c = input().split(" ")

l = int(l)
c = int(c)
matrizPrincipal = []

geraMatriz(matrizPrincipal, l, c)
imprimeMatriz(matrizPrincipal)
identificaSubMatriz(matrizPrincipal)

# ============================================================================ #