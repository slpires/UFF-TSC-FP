'''
===============================================================
== UFF - Universidade Federal Fluminense                     ==
== Tecnologia em Sistemas de Computação                      ==
== Sérgio Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1            ==
===============================================================
https://www.urionlinejudge.com.br/judge/pt/problems/view/1066
2017/02/23
'''

par = 0
impar = 0
positivo = 0
negativo = 0

for i in range(5):
    n = int(input())
    if (n % 2) == 0:
        par += 1
    else:
        impar += 1
    if n > 0:
        positivo += 1
    if n < 0:
        negativo += 1

print ("%d valor(es) par(es)" %par)
print ("%d valor(es) impar(es)" %impar)
print ("%d valor(es) positivo(s)" %positivo)
print ("%d valor(es) negativo(s)" %negativo)

# =============================================================