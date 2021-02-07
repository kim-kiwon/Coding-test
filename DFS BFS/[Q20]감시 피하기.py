#탐색 + 백트래킹

n = int(input())
arr = [] #전체 배열
teachers = [] #선생님 위치
for i in range(n):
    temp = list(input().split())
    for j in range(n):
        if temp[j] == 'T':
            teachers.append([i,j])
    arr.append(temp)

def check(x, y, d): #선생님 위치 기준 4방향 탐색. 학생 발견시 True 반환
    if d == 0:
        while y >= 0:
            if arr[x][y] == 'S':
                return True
            if arr[x][y] == 'O':
                return False
            y -= 1
    elif d == 1:
        while y < n:
            if arr[x][y] == 'S':
                return True
            if arr[x][y] == 'O':
                return False
            y += 1
    elif d == 2:
        while x >= 0:
            if arr[x][y] == 'S':
                return True
            if arr[x][y] == 'O':
                return False
            x -= 1
    elif d == 3:
        while x < n:
            if arr[x][y] == 'S':
                return True
            if arr[x][y] == 'O':
                return False
            x += 1

flag = 0 #모든 학생이 발견 안되었는가 flag.
def solve(r, count):
    global flag
    if count == 3: #장애물 세개 배치후.
        for x, y in teachers: #모든 선생님의 4방향 돌면서 check.
            for d in range(4):
                if check(x, y, d):
                    return True #발견시 현재 case 종료.
        flag = 1 #모든 학생 미발견시 flag 변경 후 종료.
        return False
    for i in range(r, n): #백트래킹으로 장애물 배치.
        for j in range(n):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                solve(r, count+1)
                arr[i][j] = 'X'

solve(0, 0)

if flag == 1:
    print("YES")
else:
    print("NO")