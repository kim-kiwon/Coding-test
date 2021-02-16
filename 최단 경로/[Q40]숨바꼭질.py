#다익스트라
import heapq

INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

distance = [INF] * (n+1)

q = []
q.append((1, 0))
distance[1] = 0
while q:
    now, dist = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (i[0], cost))

distance[0] = int(-1e9) #최댓값 영향 안주기 위해 distance[0] 매우 작게 설정.
count = 0 #최대값과 같은 개수
max_node = 0 #최대값인 노드
max_dist = max(distance) #최대값
for i in range(n, 0, -1): #거꾸로 탐지. 최대값인 노드 작은 수 되게 하려고.
    if max_dist == distance[i]:
        count += 1
        max_node = i

print(max_node, max_dist, count)
