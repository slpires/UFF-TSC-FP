# AD1 - Questão 5

# Subprogramas

def lerEntrada():
    valores = input().split()
    largura, altura = int(valores[0]), int(valores[1])

    linhas = []
    for lin in range(altura):
        texto = input()
        linha = []
        for col in range(largura):
            linha.append(texto[col])
        linhas.append(linha)
    return linhas


def encontrouTesouro(mapa):
    lin, col = 0, 0  # Posição atual no mapa.
    direcao = None  # Indica para onde andar (guarda a última seta encontrada).

    while 0 <= lin < len(mapa) and 0 <= col < len(mapa[lin]):
        atual = mapa[lin][col]

        if atual == "*":
            return True  # O tesouro foi encontrado. Parar por aqui, pois o mapa é válido.
        elif atual == "x":
            return False  # O 'x' é usado para marcar setas já visitadas. A segunda visita indica que está andando em círculos. Parar por aqui, pois o mapa não é válido.
        elif atual == "." and direcao == None:
            return False  # Se o programa chegou aqui é porque mapa[0][0] não possui uma seta. Logo, o mapa não é válido. Obs: É garantido que mapa[0][0] contenha uma seta, mas coloquei esse teste no código porque vários alunos o fizeram.
        elif atual == ">" or atual == "<" or atual == "v" or atual == "^":
            direcao = atual  # Atualizar a direção a ser seguida guardando a seta que está na posição atual.
            mapa[lin][col] = "x"  # Substituir a seta por 'x' para identificar quando está andando em círculos.

        if direcao == ">":
            col += 1
        elif direcao == "<":
            col -= 1
        elif direcao == "v":
            lin += 1
        elif direcao == "^":
            lin -= 1

    return False  # Se o programa chegou aqui então as direções levaram para fora da matriz. O mapa não é válido.


# Programa Principal
entrada = lerEntrada()
if encontrouTesouro(entrada):
    print("Esse mapa leva ao tesouro")
else:
    print("Esse mapa não leva a lugar algum")