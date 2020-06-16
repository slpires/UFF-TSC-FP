'''
===============================================================
== UFF - Universidade Federal Fluminense                     ==
== Tecnologia em Sistemas de Computação                      ==
== Sérgio Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1            ==
===============================================================
https://www.urionlinejudge.com.br/judge/pt/problems/view/1015
2017/02/21
'''

ponto1 = input()
x1, y1 = ponto1.split(" ")
x1 = float(x1)
y1 = float(y1)

ponto2 = input()
x2, y2 = ponto2.split(" ")
x2 = float(x2)
y2 = float(y2)

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

print("%1.4f" %distancia)

# =============================================================