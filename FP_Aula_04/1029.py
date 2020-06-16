'''
===============================================================
== UFF - Universidade Federal Fluminense                     ==
== Tecnologia em Sistemas de Computação                      ==
== Sérgio Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1            ==
===============================================================
https://www.urionlinejudge.com.br/judge/pt/problems/view/1029
Problema: Time limit exceeded
2017/03/04
'''

# Calcula Fibonacci(i)

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)

# Calcula a quantidade de chamadas recursivas para Fibonacci(i)

def chamadas(i):
    if 0 <= i <= 1:
        return 1
    else:
        return chamadas(i-1) + chamadas(i-2) + 1

# Programa principal

quantidadeNumeros = int(input())

Numeros = [None] * quantidadeNumeros

for k in range(len(Numeros)):
    Numeros[k] = int(input())

for j in Numeros:
    if 0 <= j <= 1:
        calls = 1
    else:
        calls = chamadas(j) - 1
    print("fib(%d) = %d calls = %d" %(j, calls, fibonacci(j)))

# =============================================================