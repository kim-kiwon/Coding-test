#서로소 집합.
#연결 되었는지 확인하는 문제. 서로소 집합으로 해결

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

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
    temp = [0] + list(map(int, input().split()))
    for j in range(1, n+1):
        if temp[j] == 1:
            union_parent(parent, i, j)

schedule = list(map(int, input().split()))
for i in range(1, len(schedule)):
    if find_parent(parent, schedule[i-1]) != find_parent(parent, schedule[i]):
        print("NO")
        break
    elif i == len(schedule)-1:
        print("YES")