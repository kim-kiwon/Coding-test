#플로이드 워셜 : 모든 노드에서 모든 노드로의 최소 비용
from sys import stdin
input = stdin.readline

INF = int(1e9) #무한
n = int(input()) #노드 수
m = int(input()) #간선 수
graph = [[INF] * (n+1) for _ in range(n+1)] #노드 수x노드 수의 2차원 그래프. 무한으로 초기화

#자기 자신에게 가는 비용 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#각 간선 연결정보 입력받아. 그 값 이용 인접 노드간 비용 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

#플로이드 워셜 수행
for k in range(1, n+1): #특정 노드 k에 대해.
    for a in range(1, n+1): #a에서 출발.
        for b in range(1, n+1): #b로 도착.
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) #현재 a->b와. a->k->b중 더 작은값으로 a->b갱신.

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("IFINITY", end = ' ')
        else:
            print(graph[a][b], end = ' ')
    print()