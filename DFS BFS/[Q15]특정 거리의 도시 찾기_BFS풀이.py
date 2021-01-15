#bfs 가능.
#왜? 간선의 비용이 모두 같은 최단경로 탐색이므로.
#출발점에서 시작해서 밟는대로 최단경로가 된다.
#간선의 비용이 다르면 다익스트라로 풀어야함.
#돌아서 가는게 더 빠를 수 있으므로.

from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

finish = [-1] * (n+1)

def bfs(start):
    q = deque()
    q.append(start)
    finish[start] = 0
    while q:
        a = q.popleft()
        for b in graph[a]:
            if finish[b] == -1:
                finish[b] = finish[a] + 1
                q.append(b)

bfs(x)

flag = 0

for i in range(1, n+1):
    if finish[i] == k:
        flag = 1
        print(i)

if flag == 0:
    print(-1)