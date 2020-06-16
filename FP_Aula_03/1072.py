'''
===============================================================
== UFF - Universidade Federal Fluminense                     ==
== Tecnologia em Sistemas de Computação                      ==
== Sérgio Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1            ==
===============================================================
https://www.urionlinejudge.com.br/judge/pt/problems/view/1072
2017/02/24
'''

numeros = int(input())
dentro = 0
fora = 0

for v in range(0,numeros):
    valor = int(input())
    if 10 <= valor <= 20:
        dentro += 1
    else:
        fora += 1

print("%d in" %dentro)
print("%d out" %fora)

# =============================================================