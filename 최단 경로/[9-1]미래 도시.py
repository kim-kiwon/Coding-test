from sys import stdin
import heapq

input = stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1)) #양방향 연결이므로 b의 연결 노드에도 a를 추가해줄 것.

x, k = map(int, input().split())

distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
first = distance[k]

distance = [INF] * (n+1) #한번 다익스트라 수행하면 distance가 오염됨. INF로 초기화.

dijkstra(k)
second = distance[x]

result = first+second
if result >= INF:
    print(-1)
else:
    print(result)
