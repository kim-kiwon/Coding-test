N, M = map(int, input().split())
r, c, d = map(int, input().split())

maparr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    maparr.append(temp)

visit = [[0 for _ in range(M)] for _ in range(N)]
# d = 0: 북. 1: 동. 2: 남. 3: 서.
def turn():
    global d
    d -= 1
    if d < 0:
        d = 3

def canvisit(a, b):
    if visit[a][b] == 0 and maparr[a][b] == 0:
        return True

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
#각 d (0~3) 에서의 전진시 이동벡터
turn_count = 0
result = 1
while 1:
    turn()
    nr = r + dr[d]
    nc = c + dc[d]
    if canvisit(nr, nc):
        r = nr
        c = nc
        visit[r][c] = 1
        result += 1
        turn_count = 0
        continue
    else:
        turn_count += 1
    if turn_count == 4:
        nr = r - dr[d]
        nc = c - dc[d]
        if maparr[nr][nc] == 0:
            r = nr
            c = nc
            turn_count = 0
        else:
            break

print(result)