n, m = map(int, input().split())
arr = []
for _ in range(n):
    temp = list(map(int, input()))
    arr.append(temp)

visit = [[0 for _ in range(m)]for _ in range(n)]
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if arr[x][y] == 0 and visit[x][y] == 0:
        visit[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)