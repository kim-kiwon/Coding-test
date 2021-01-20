#입력의 개수가 적어 플로이드로도 충분히 해결 가능.
INF = int(1e9)
n, m = map(int, input().split())
arr = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    arr[a][a] = 0

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if arr[i][j] != INF or arr[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)