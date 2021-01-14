#크루스칼 알고리즘 : 사이클 없는 모든 노드가 연결된 그래프 만들기.
#간선을 cost 별로 정렬. 해당 간선이 사이클 생성하는지 체크 후, 서로소 집합에 넣어준다.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()#간선을 비용으로 정렬.

#모든 간선에 대해 사이클 생성 하지 않으면. union_parent로 서로소 집합에 넣어주고 비용 더해줌.
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)