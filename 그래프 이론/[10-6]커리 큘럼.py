from collections import deque
import copy

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)

for i in range(1, n+1): #i번째 노드정보 입력.
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]: #인덱스 1부터 시작해서. 끝에서 -1하기 전것 까지 가져옴. range에서 마지막건 포함 X
                         #즉 선수강 필요 과목들만 가져온다.
        indegree[i] += 1 #선과목 수만큼 후과목의 진입차수에 추가.
        graph[x].append(i) #선과목->후과목 되도록. 선과목의 리스트에 후과목 추가.
def topology_sort():
    q = deque()
    result = copy.deepcopy(time)
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]: #now 들어야 들을수 있는 후과목들 i
            result[i] = result[now] + time[i] #후과목 시간 : 선과목의 최종 시간 + 후과목 시간
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()
