# 単純パーセプトロン　応用情報技術者試験　令和1年過去問
def simple_perceptron(X, Y):
    for out in range(NC):
        ytemp = BY
        for i in range(NI):
            ytemp += X[out][i] * WY[i]

        if ytemp > 0:
            Y[out] = 1
        else:
            Y[out] = 0

        print('x1:', X[out][0], 'x2:', X[out][1], 'Y:', Y[out])


NI = 2
NC = 4
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [0]*NC
WY = [0.5, 0.5]
BY = -0.2

simple_perceptron(X, Y)