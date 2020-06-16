'''
===============================================================
== UFF - Universidade Federal Fluminense                     ==
== Tecnologia em Sistemas de Computação                      ==
== Sérgio Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1            ==
===============================================================
https://www.urionlinejudge.com.br/judge/pt/problems/view/1071
2017/02/23
'''

x = int(input())
y = int(input())

somaImpar = 0

if (x % 2 == 0) and (x <= y):
    for n in range((x+1),y,2):
        somaImpar += n
elif (x % 2 == 0) and (x > y):
    for n in range((x-1),y,-2):
        somaImpar += n
elif (x % 2 != 0) and (x <= y):
    for n in range(x+2,y,2):
        somaImpar += n
elif (x % 2 != 0) and (x > y):
    for n in range(x-2,y,-2):
        somaImpar += n

print(somaImpar)

# =============================================================