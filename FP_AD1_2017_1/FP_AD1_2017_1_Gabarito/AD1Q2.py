# AD1 - Questão 2

# Subprogramas

def obterPontos():
    qtdPontos = int(input())
    pontos = []
    for i in range(qtdPontos):
        linhaLida = input()
        x = int(linhaLida.split()[0])
        y = int(linhaLida.split()[1])
        pontos.append([x, y])
    return pontos


def extremos(pontos):
    faixaX = (pontos[0][0], pontos[0][0])
    faixaY = (pontos[0][1], pontos[0][1])
    for pt in pontos:
        if pt[0] < faixaX[0]:
            faixaX = (pt[0], faixaX[1])
        elif pt[0] > faixaX[1]:
            faixaX = (faixaX[0], pt[0])
        if pt[1] < faixaY[0]:
            faixaY = (pt[1], faixaY[1])
        elif pt[1] > faixaY[1]:
            faixaY = (faixaY[0], pt[1])
    return (faixaX, faixaY)


def analisa(pontos, minimo, maximo):
    (xMin, yMin) = minimo
    (xMax, yMax) = maximo
    qtdPontosDentro = 0
    print("Pontos dentro do retângulo:")
    for [x, y] in pontos:
        if xMin <= x <= xMax and yMin <= y <= yMax:
            print(x, y)
            qtdPontosDentro += 1
    print("Total de Pontos:", qtdPontosDentro)
    return None


# Programa Principal
vetorDePontos = obterPontos()
((xMin, xMax), (yMin, yMax)) = extremos(vetorDePontos)
print("xMin =", xMin)
print("yMin =", yMin)
print("xMax =", xMax)
print("yMax =", yMax)
analisa(vetorDePontos, (xMin, yMin), (xMax // 2, yMax // 2))