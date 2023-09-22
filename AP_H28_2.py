# 魔法陣　応用情報技術者試験　平成28年過去問
# 番兵なし
def mahoujin(N, houjin):
    y = N-1
    x = (N+1)//2-1
    suuji = 1
    houjin[y][x]= suuji

    while(suuji!=N**2):
        yb = y
        xb = x

        y += 1
        x += 1

        if y > N-1:
            y = 0
        if x > N-1:
            x = 0

        if houjin[y][x] != 0:
            y = yb - 1
            x = xb

        suuji += 1
        houjin[y][x] = suuji
    return houjin

N = 5

houjin = [[0]*(N) for _ in range(N)]
print("")

houjin2 = mahoujin(N, houjin)
for i in range(N):
    for j in range(N):
        if j==N-1:
            print(houjin2[i][j])
        else:
            print(houjin2[i][j],end =" ")