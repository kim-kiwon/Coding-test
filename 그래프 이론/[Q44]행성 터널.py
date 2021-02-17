#크루스칼 알고리즘 이용 최소신장트리 구하기.

#부모찾기.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#부모결합. 두 노드가 연결되면 큰 노드의 부모 = 작은 노드 번호
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 부모가 이미 같은 노드(같은 집합) 간에 연결하면 사이클 생기고 MST깨짐.
n = int(input())

#부모값 초기화
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

#모든 간선 확인 -> 시간초과. x y z 별로 정렬후 인접한 간선만 삽입시키자. a->b < a->c 이용.
planet = []
edges = []
for i in range(n):
    x, y, z = map(int, input().split())
    planet.append((x, y, z, i)) #사이클 유무 확인 위해 노드 번호 삽입.

for i in range(3):
    planet.sort(key = lambda x : x[i])
    before = planet[0][3]
    for j in range(1, n):
        current = planet[j][3]
        edges.append([abs(planet[j][i] - planet[j-1][i]), before, current]) #사이클 유무 확인 위함.
        before = current

edges.sort() #edge를 cost에 따라 정렬.
count = 0
result = 0

for dist, start, end in edges:
    if find_parent(parent, start) != find_parent(parent, end):
        result += dist
        union_parent(parent, start, end)
        count += 1
    if count == n:
        break
print(result)
