#다익스트라: 한 노드에서 다른 모든 노드로의 최소비용
from sys import stdin
import heapq

input = stdin.readline
INF = int(1e9) # 현재 기준 갈 수 없는 노드 거리 무한으로 설정.

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)] # graph[1] : 1번노드와 연결된 다른 노드들 저장.
distance = [INF] * (n+1) # 최단 경로 리스트 무한으로 초기화.

for _ in range(m):
    a, b, c = map(int ,input().split())
    graph[a].append((b,c))
    # graph[1][0] : 1번노드와 연결된 첫번째 노드. graph[1][0][0] : 그 노드 번호. graph[1][0][1]: 그 노드 거리

def dijkstra(start):
    q = [] #heapq로 사용할 리스트 선언.
    heapq.heappush(q, (0, start)) # 시작 노드를 (거리, 노드번호)로 하여 heapq에 삽입.
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) #heapq에서 pop(기본이 최소힙. 가장 거리가 가까운 노드 꺼냄)
        if distance[now] < dist: #해당 노드가 이미 처리되어 distance 값이 더 낮다면.
            continue
        for i in graph[now]:
            cost = dist + i[1] #새로 확정한 노드와 인접한 노드를. 새로 확정한 노드 거쳐서 가는경우
            if cost < distance[i[0]]: #그 값이 현재보다 더 작으면 갱신 후 heapq에 삽입.
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
