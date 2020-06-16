'''
===============================================================
== UFF - Universidade Federal Fluminense                     ==
== Tecnologia em Sistemas de Computação                      ==
== Sérgio Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1            ==
===============================================================
https://www.urionlinejudge.com.br/judge/pt/problems/view/1930
AAAA/MM/DD
'''

tomadas = input()
t1, t2, t3, t4 = tomadas.split(" ")
t1 = int(t1)
t2 = int(t2)
t3 = int(t3)
t4 = int(t4)

numeroMaximo = (t1 - 1) + (t2 - 1) + (t3 - 1) + t4

print(numeroMaximo)

# =============================================================