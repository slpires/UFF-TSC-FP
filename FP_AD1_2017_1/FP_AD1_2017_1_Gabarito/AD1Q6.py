# AD1 - Questão 6

# Subprogramas

def lerAmbiente(altura, largura):
    mapa = []
    for lin in range(altura):
        texto = input()
        linha = []
        for col in range(largura):
            linha.append(texto[col])
        mapa.append(linha)
    return mapa


def escreverAmbiente(mapa):
    for lin in range(len(mapa)):
        for col in range(len(mapa[lin])):
            print(mapa[lin][col], end="")
        print()
    print()


def espalharInformacao(mapa, lin, col):
    mapa[lin][col] = "I"
    if lin - 1 >= 0 and mapa[lin - 1][col] == "F":
        espalharInformacao(mapa, lin - 1, col)
    if lin + 1 < len(mapa) and mapa[lin + 1][col] == "F":
        espalharInformacao(mapa, lin + 1, col)
    if col - 1 >= 0 and mapa[lin][col - 1] == "F":
        espalharInformacao(mapa, lin, col - 1)
    if col + 1 < len(mapa[lin]) and mapa[lin][col + 1] == "F":
        espalharInformacao(mapa, lin, col + 1)


# Programa Principal
par = input().split()
n, m = int(par[0]), int(par[1])

while n != 0 and m != 0:
    ambiente = lerAmbiente(n, m)

    for i in range(n):
        for j in range(m):
            if ambiente[i][j] == "I":
                espalharInformacao(ambiente, i, j)
    escreverAmbiente(ambiente)

    par = input().split()
    n, m = int(par[0]), int(par[1])