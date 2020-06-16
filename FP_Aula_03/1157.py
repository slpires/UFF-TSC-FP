'''
===============================================================
== UFF - Universidade Federal Fluminense                     ==
== Tecnologia em Sistemas de Computação                      ==
== Sérgio Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1            ==
===============================================================
https://www.urionlinejudge.com.br/judge/pt/problems/view/1157
2017/02/23
'''

n = int(input())

for d in range(1,n+1):
    r = n % d
    if r == 0:
        print(d)

# =============================================================