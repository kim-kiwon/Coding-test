from sys import stdin
import heapq

INF = int(1e9)
input = stdin.readline

n, m, c = map(int ,input().split())
graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] < cost:
                continue
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
maxval = -int(1e9)

for i in range(1, n+1):
    if distance[i] != INF:
        count += 1
        maxval = max(maxval, distance[i])

print(count-1, maxval) #시작 노드 제외