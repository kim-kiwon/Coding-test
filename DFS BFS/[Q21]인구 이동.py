#반복 BFS
from collections import deque

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    visited[x][y] = True
    united = [(x, y)] # 연합이 된 국가들
    u_count = 1 # 연합 국가 수
    u_sum = arr[x][y] #연합 국가 합
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                    global union_on
                    union_on = True # 이번 회차에 연합이 발생했는가.
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    u_sum += arr[nx][ny]
                    u_count += 1
                    united.append((nx, ny))
    for i, j in united: #연합국들 값 갱신
        arr[i][j] = u_sum // u_count
    return

result = 0

while True:
    union_on = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False: #방문하지 않은 국가에 대해 bfs 실행
                bfs(i, j)
    if union_on == False: #이번 회차 모든 국가 방문해도 BFS 없다면. 탈출.
        break
    result += 1

print(result)