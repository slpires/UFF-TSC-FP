'''
===============================================================
== UFF - Universidade Federal Fluminense                     ==
== Tecnologia em Sistemas de Computação                      ==
== Sérgio Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1            ==
===============================================================
https://www.urionlinejudge.com.br/judge/pt/problems/view/1043
2017/02/25
'''

ladosInicial = input().split(" ")

ladosFinal = list(ladosInicial)

for i in range(0,len(ladosFinal)-1):
    for j in range(i+1,len(ladosFinal)):
        if float(ladosFinal[i]) < float(ladosFinal[j]):
            temp = ladosFinal[i]
            ladosFinal[i] = ladosFinal[j]
            ladosFinal[j] = temp

if float(ladosFinal[0]) >= float(ladosFinal[1]) + float(ladosFinal[2]):
    area = (float(ladosInicial[0]) + float(ladosInicial[1])) * float(ladosInicial[2]) / 2
    print("Area = %3.1f" %area)
else:
    perimetro = float(ladosFinal[0]) + float(ladosFinal[1]) + float(ladosFinal[2])
    print("Perimetro = %3.1f" % perimetro)

# =============================================================