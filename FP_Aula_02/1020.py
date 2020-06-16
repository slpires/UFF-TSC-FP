'''
===============================================================
== UFF - Universidade Federal Fluminense                     ==
== Tecnologia em Sistemas de Computação                      ==
== Sérgio Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1            ==
===============================================================
https://www.urionlinejudge.com.br/judge/pt/problems/view/1020
2017/02/21
'''

idadeDias = int(input())

idadeAnos  = idadeDias // 365
idadeMeses = (idadeDias % 365) // 30
idadeDias  = (idadeDias % 365) % 30

print("%1d ano(s)" %idadeAnos)
print("%1d mes(es)" %idadeMeses)
print("%1d dia(s)" %idadeDias)

# =============================================================