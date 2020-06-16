'''
================================================================================
== UFF - Universidade Federal Fluminense                                      ==
== Tecnologia em Sistemas de Computação                                       ==
== Sérgio Luís de Oliveira Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1                             ==
================================================================================
AD1 - QUESTÃO 4
'''

# Subprogramas

def verificaPerfeito(valor):
    if valor > 1:
        soma = 0
        for k in range(1,valor):
            resto = valor % k
            if resto == 0:
                soma += k
        if soma == valor:
            resposta = True
        else:
            resposta = False
    else:
        resposta = False
    return resposta


# Programa Principal

n = int(input())

numeros = [None]*n

for i in range(n):
    numeros[i] = int(input())

for j in range(n):
    if verificaPerfeito(numeros[j]) == True:
        print("%d é perfeito" %numeros[j])
    else:
        print("%d não é perfeito" %numeros[j])

# ============================================================================ #