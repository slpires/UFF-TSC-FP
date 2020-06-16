'''
================================================================================
== UFF - Universidade Federal Fluminense                                      ==
== Tecnologia em Sistemas de Computação                                       ==
== Sérgio Luís de Oliveira Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1                             ==
================================================================================
AD1 - QUESTÃO 1
'''

# Programa Principal

ponto = input().split(" ")
x = float(ponto[0])
y = float(ponto[1])

xTotal = 0
yTotal = 0
qtdPontos = 0

if (x == 0) and (y == 0):
    print ("Não existem pontos!")
else:
    while (x != 0) and (y != 0):
        xTotal = xTotal + x
        yTotal = yTotal + y
        qtdPontos = qtdPontos + 1
        ponto = input().split(" ")
        x = float(ponto[0])
        y = float(ponto[1])
    print("%1.2f %1.2f" %((xTotal/qtdPontos), (yTotal/qtdPontos)))

# ============================================================================ #