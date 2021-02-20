# AD1 - Questão 4

# Subprogramas

def ehPerfeito(numero):
    soma = 0
    for divisor in range(1, numero - 1):
        if numero % divisor == 0:
            soma = soma + divisor
    return soma == numero


# Programa Principal
n = int(input())
for i in range(n):
    x = int(input())
    if ehPerfeito(x):
        print(x, "é perfeito")
    else:
        print(x, "não é perfeito")