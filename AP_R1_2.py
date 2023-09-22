# 3層パーセプトロン　応用情報技術者試験　令和1年過去問
def three_layer_perceptron(X, Y):
    for out in range(NC):
        ytemp = BY
        for mid in range(NM):
            mtemp = BM[mid]
            for i in range(NI):
                mtemp += X[out][i] * WM[mid][i]

            if mtemp > 0:
                M[out][mid] = 1
            else:
                M[out][mid] = 0

            ytemp += M[out][mid] * WY[mid]
        
        if ytemp > 0:
            Y[out] = 1
        else:
            Y[out] = 0

        print('x1:', X[out][0], 'x2:', X[out][1], 'Y:', Y[out])


NI = 2
NC = 4
NM = 2
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [0]*NC
M = [[0]*NM for _ in range(NC)]

# 排他的論理和
WY = [0.5, 0.5]
WM = [[0.5, 0.5], [-0.5, -0.5]]
BY = -0.6
BM = [-0.2, 0.7]

three_layer_perceptron(X, Y)