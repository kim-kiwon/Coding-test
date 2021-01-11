from collections import deque

n, m = map(int ,input().split())
arr = []
for _ in range(n):
    temp = list(map(int, input()))
    arr.append(temp)

visit = [[0 for _ in range(m)]for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visit[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if visit[nx][ny] != 0:
                continue
            queue.append((nx, ny))
            print(queue)
            visit[nx][ny] = visit[x][y] + 1

bfs(0, 0)
print(visit)
print(visit[n-1][m-1])