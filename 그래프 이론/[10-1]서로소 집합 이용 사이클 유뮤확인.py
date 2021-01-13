#서로소 집합 : 무방향 그래프에서 사이클 판별에 활용

#x가 속한 집합의 루트 노드를 찾는 함수.
def find_parent(parent, x):
    #루트 노드가 될 때까지 계속 재귀. 루트 노드 도착시 해당 값 반환
    if parent[x] != x:
        parent[x] =  find_parent(parent, parent[x])
    return parent[x]

#a가 속한 집합과 b가 속한 집합을 union하는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    #두 root 노드 중 더 작은 값을 가진놈이 부모가됨.

v, e = map(int, input().split()) #노드 개수. 간선(union 연산) 수 입력.
parent = [0] * (v + 1) # 부모 테이블.

#초기 부모 = 자기 자신
for i in range(1, v+1):
    parent[i] = i

cycle = False

#union 연산 수행. a, b 가 속한 집합을 union
for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)
    #사이클 판별법 : 모든 간선 확인. 연결된 노드끼리 서로소 집합으로 만듦.(union 수행. parent 갱신)
    #이미 같은 집합 인 것끼리 union 재수행 하게되면 cycle 발생한 것.
if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")

