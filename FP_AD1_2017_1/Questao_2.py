'''
================================================================================
== UFF - Universidade Federal Fluminense                                      ==
== Tecnologia em Sistemas de Computação                                       ==
== Sérgio Luís de Oliveira Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1                             ==
================================================================================
AD1 - QUESTÃO 2
'''

# Programa Principal

qtdPontos = int(input())

pontos = []
valoresX = []
valoresY = []

for i in range(qtdPontos):
    ponto = input().split(" ")
    pontos.append(ponto)
    valoresX.append(int(ponto[0]))
    valoresY.append(int(ponto[1]))

xMin = min(valoresX)
yMin = min(valoresY)
xMax = max(valoresX)
yMax = max(valoresY)

print("xMin = %d" %xMin)
print("yMin = %d" %yMin)
print("xMax = %d" %xMax)
print("yMax = %d" %yMax)
print("Pontos dentro do retângulo:")

qtdPontosDentro = 0

for j in range(qtdPontos):
    if (xMin <= int(pontos[j][0]) <= xMax//2) and (yMin <= int(pontos[j][1]) <= yMax//2):
        qtdPontosDentro = qtdPontosDentro + 1
        print("%s %s" %(pontos[j][0], pontos[j][1]))

print("Total de Pontos: %d" %qtdPontosDentro)

# ============================================================================ #