'''
===============================================================
== UFF - Universidade Federal Fluminense                     ==
== Tecnologia em Sistemas de Computação                      ==
== Sérgio Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1            ==
===============================================================
https://www.urionlinejudge.com.br/judge/pt/problems/view/1042
2017/02/25
'''

listaInicial = input().split(" ")

listaFinal = list(listaInicial)

for i in range(0,len(listaFinal)-1):
    for j in range(i+1,len(listaFinal)):
        if int(listaFinal[i]) > int(listaFinal[j]):
            temp = listaFinal[i]
            listaFinal[i] = listaFinal[j]
            listaFinal[j] = temp

for k in range(len(listaFinal)):
    print(listaFinal[k])

print()

for k in range(len(listaInicial)):
    print(listaInicial[k])

# =============================================================