#Deepcopy와 재귀 이용
import copy

fishes = [[-1, -1]] + [[0, 0] for _ in range(16)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

data = [[0] * 4 for _ in range(4)]

for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        data[i][j] = [temp[j * 2], temp[j * 2 + 1] - 1]


def find_fish(data, index):
    for i in range(4):
        for j in range(4):
            if data[i][j][0] == index:
                return (i, j)
    return None

def turn_left(direc):
    return (direc + 1) % 8

def move_fish(sx, sy, data):
    for i in range(1, 17):
        pos = find_fish(data, i) #i번째 물고기의 위치
        if pos != None:
            x, y, direc = pos[0], pos[1], data[pos[0]][pos[1]][1]
            for j in range(8):
                nx = x + dx[direc]
                ny = y + dy[direc]
                if 0 <= nx < 4 and 0 <= ny< 4:
                    if not(nx == sx and ny == sy):
                        data[x][y][1] = direc
                        data[x][y], data[nx][ny] = data[nx][ny], data[x][y]
                        break
                direc = turn_left(direc)


def move_shark(sx, sy, data):
    q = []
    direc = data[sx][sy][1]
    for i in range(4):
        sx += dx[direc]
        sy += dy[direc]
        if sx < 0 or sx >= 4 or sy < 0 or sy >= 4:
            continue
        if data[sx][sy][0] != -1:
            q.append((sx, sy))
    return q

result = 0
def solve(sx, sy, data, score):
    global result
    data = copy.deepcopy(data)
    score += data[sx][sy][0]
    data[sx][sy][0] = -1
    move_fish(sx, sy, data)
    q = move_shark(sx, sy, data)
    if len(q) == 0:
        result = max(score, result)
        return
    for x, y in q:
        solve(x, y, data, score)

solve(0, 0, data, 0)
print(result)