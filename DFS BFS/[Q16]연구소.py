#백트래킹 + DFS문제.
import copy
n, m = map(int ,input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

result = -int(1e9)
def dfs(count, r):
    global result, temp
    if count == 3:
        temp = copy.deepcopy(arr)
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        score = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    score += 1
        result = max(result, score)
        return
    for i in range(r, n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(count + 1, i)
                arr[i][j] = 0

dfs(0, 0)
print(result)