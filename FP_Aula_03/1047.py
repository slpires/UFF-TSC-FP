'''
===============================================================
== UFF - Universidade Federal Fluminense                     ==
== Tecnologia em Sistemas de Computação                      ==
== Sérgio Pires - 131.130.50290 (CEDERJ) - 113.071.254 (UFF) ==
== EAD05029 - Fundamentos de Programação - 2017/1            ==
===============================================================
https://www.urionlinejudge.com.br/judge/pt/problems/view/1047
2017/02/25
'''

lista = input().split(" ")

horaInicial = int(lista[0])
minutoInicial = int(lista[1])
horaFinal = int(lista[2])
minutoFinal = int(lista[3])

duracaoMinutos = minutoFinal - minutoInicial
duracaoHoras = horaFinal - horaInicial

if duracaoHoras <= 0:
    duracaoHoras += 24

if duracaoMinutos < 0:
    duracaoMinutos += 60
    duracaoHoras -= 1

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(duracaoHoras, duracaoMinutos))

# =============================================================