n = int(input())
k = int(input())

arr = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    x, y = map(int, input().split())
    arr[x][y] = 1

l = int(input())
rotate = []
for _ in range(l):
    a, c = input().split()
    rotate.append((int(a), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def solution():
    x, y = 1, 1
    arr[1][1] = 2
    direction = 0
    time = 0
    index = 0
    q = [(1, 1)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and arr[nx][ny] != 2:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                arr[px][py] = 0
            if arr[nx][ny] == 1:
                arr[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if time == rotate[index][0]:
            direction = turn(direction, rotate[index][1])
            if index < len(rotate) - 1:
                index += 1
    return time

print(solution())