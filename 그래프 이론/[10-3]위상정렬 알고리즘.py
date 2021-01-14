#위상정렬 알고리즘 : 방향 그래프로 순서가 주어질 경우. 모든 노드를 순서에 거스르지 않고 정렬.
#선수과목 고려한 수강신청이 주된 문제.
#진입차수 0 인 노드 큐에 삽입. 큐에서 제거시 해당 노드에서 나가는 간선 모두제거. 반복
#큐가 비었는데 방문하지 않는 노드가 남았다 -> 사이클존재 (남은 노드 중에 진입차수 0 인 노드가 없게되므로)

from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1) #진입차수 0으로 초기화
graph = [[] for i in range(v+1)]

#간선 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] +=1 #b 진입차수 증가

def topology_sort():
    result = []
    q = deque()

    #진입차수 0인 노드 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft() #큐에서 꺼내고
        result.append(now) #결과에 넣기.
        #해당 원소와 연결된 노드 진입차수 1 빼주기
        for i in graph[now]:
            indegree[i] -= 1
            #새로 진입차수 0인 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    #결과 출력
    for i in result:
        print(i, end=' ')


topology_sort()

