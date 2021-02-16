#다익스트라 + 탐색
import heapq
INF = int(1e9)
t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(t):
    n = int(input())
    graph = [] #각 칸 비용 list로 입력받음.
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    distance = [[INF] * (n) for _ in range(n)]
    q = []
    q.append((0, 0, graph[0][0]))
    while q:
        x, y, dist = heapq.heappop(q)
        if dist > distance[x][y]: #현재 칸이 더 작은비용으로 갱신되어있다면.
            continue
        for i in range(4): #현재 칸과 연결된 칸 => 상하좌우(탐색)
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny] #cost = 전칸까지 비용 + 현재칸 비용
                if cost < distance[nx][ny]: #cost가 현재최소비용보다 작다면 갱신 후 큐 삽입.
                    distance[nx][ny] = cost
                    heapq.heappush(q, (nx, ny, cost))
    print(distance[n-1][n-1])
