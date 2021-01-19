from sys import stdin

input = stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

distance = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    distance[a][b] = min(distance[a][b], cost)

for a in range(1, n+1):
    distance[a][a] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if distance[a][b] == INF:
            distance[a][b] = 0
        print(distance[a][b], end = " ")
    print()