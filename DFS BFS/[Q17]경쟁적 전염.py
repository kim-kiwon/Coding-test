#매 초 마다 완전탐색하면서. 바이러스의 위치를 저장하고.
#바이러스 번호 별로 sort후 전파를 진행시키자.
#deque는 sort가 없으므로. sort후 deque로 옮길것.

from collections import deque

n, k = map(int, input().split())
arr = []
data = []

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] != 0 :
            data.append((temp[j], 0, i, j))
    arr.append(temp)
target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data.sort()
q = deque(data)

while q:
    type, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if arr[nx][ny] == 0:
                arr[nx][ny] = type
                q.append((type, s + 1, nx, ny))

print(arr[target_x - 1][target_y - 1])