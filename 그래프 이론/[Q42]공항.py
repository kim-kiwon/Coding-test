#그래프 없이도. 최대 탑승구의 번호에 도킹시키면 되지않을까?
#O(GP)라서 시간초과난다.

#서로소 집합 이용. parent가 0이면 앞에 다찼다. 즉 도킹할 수 없다는 의미.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

g = int(input())
p = int(input())

parent = [0] * (g+1)
for i in range(1, g+1):
    parent[i] = i

count = 0

for _ in range(p):
    data = find_parent(parent, int(input()))
    if data == 0:
        break
    union_parent(parent, data, data-1)
    count += 1

print(count)