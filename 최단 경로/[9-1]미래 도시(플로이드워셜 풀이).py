from sys import stdin
import heapq

input = stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

distance = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            distance[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    distance[a][b] = 1
    distance[b][a] = 1

x, k = map(int, input().split())

for q in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            distance[a][b] = min(distance[a][b], distance[a][q] + distance[q][b])

result = distance[1][k] + distance[k][x]

if result >= INF:
    print(-1)
else:
    print(result)
