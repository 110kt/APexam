# 魔法陣　応用情報技術者試験　平成28年過去問
# 番兵あり
def syokika(N, houjin):
    for y in range(N):
        for x in range(N):
            houjin[y][x] = 0
        houjin[y][N] = SOTO_MIGI

    for x in range(N):
        houjin[N][x] = SOTO_SHITA

    houjin[N][N] = SOTO_KADO
    return houjin


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

        if houjin[y][x] == SOTO_SHITA:
            y = 0
        
        elif houjin[y][x] == SOTO_MIGI:
            x = 0
        
        elif houjin[y][x] == SOTO_KADO:
            y = 0
            x = 0
    
        if houjin[y][x] != 0:
            y = yb - 1
            x = xb
        
        suuji += 1
        houjin[y][x] = suuji
    return houjin

N = 5
SOTO_MIGI = N**2+N
SOTO_SHITA = N**2+2*N
SOTO_KADO = N**2+3*N

houjin = [[0]*(N+1) for _ in range(N+1)]
houjin1 = syokika(N, houjin)
# for i in range(N+1):
#     print(*houjin[i])
print("")

houjin2 = mahoujin(N, houjin1)
for i in range(N):
    for j in range(N):
        if j==N-1:
            print(houjin2[i][j])
        else:
            print(houjin2[i][j],end =" ")