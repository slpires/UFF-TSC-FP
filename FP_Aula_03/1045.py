'''
===============================================================
== UFF - Universidade Federal Fluminense                     ==
== Tecnologia em Sistemas de Computação                      ==
== Sérgio Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1            ==
===============================================================
https://www.urionlinejudge.com.br/judge/pt/problems/view/1045
2017/02/25
'''

lados = input().split(" ")

for i in range(0,len(lados)-1):
    for j in range(i+1,len(lados)):
        if float(lados[i]) < float(lados[j]):
            temp = lados[i]
            lados[i] = lados[j]
            lados[j] = temp

a = float(lados[0])
b = float(lados[1])
c = float(lados[2])

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    if a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    if a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")
    if (a == b) and (b == c):
        print("TRIANGULO EQUILATERO")
    elif (a == b) or (a == c) or (b == c):
        print("TRIANGULO ISOSCELES")

# =============================================================