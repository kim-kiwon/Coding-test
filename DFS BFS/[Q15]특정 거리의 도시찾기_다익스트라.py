#다익스트라 이용 풀이
#한 지점에서 다른 지점으로의 최단경로이므로 다익스트라로도 해결가능.

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

distance = [INF] * (n+1)

def dijkstrea(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstrea(x)

flag = 0

for i in range(1, n+1):
    if distance[i] == k:
        flag = 1
        print(i)

if flag == 0:
    print(-1)