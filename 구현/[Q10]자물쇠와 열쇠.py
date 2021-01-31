def rotate_2d(arr, d): #2D 행렬 회전시키는 함수.
    length = len(arr)
    newarr = [[0] * length for _ in range(length)]
    if d == 0:
        return arr
    elif d == 1:
        for i in range(length):
            for j in range(length):
                newarr[j][length - 1 - i] = arr[i][j]
    elif d == 2:
        for i in range(length):
            for j in range(length):
                newarr[length - 1 - i][length - 1 - j] = arr[i][j]
    elif d == 3:
        for i in range(length):
            for j in range(length):
                newarr[length - 1 - j][i] = arr[i][j]
    return (newarr)

def check(data): #자물쇠의 모든 칸을 1로 채웠는지 반환하는 함수.
    n = len(data) // 3
    for i in range(n):
        for j in range(n):
            if data[i + n][j + n] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    data = [[0] * (3 * n) for _ in range(3 * n)] #자물쇠를 3배 늘린 배열 data. 키를 이동시키며 결과를 도출하기 위해.
                                                 #자물쇠 배열 > 키 배열 이므로. 자물쇠 배열 크기 기준 3배 하면됨.
    #data배열에 복사.
    for i in range(n):
        for j in range(n):
            data[i + n][j + n] = lock[i][j]

    for t in range(4): #t: 키 회전 시키기 위한 변수.
        turn_key = rotate_2d(key, t)
        for i in range(2 * n): #i, j: data에서 key 놓기 시작하는 위치 인덱스.
            for j in range(2 * n):
                for r in range(m): # r,c : key의 인덱스.
                    for c in range(m):
                        data[i + r][j + c] += turn_key[r][c] #키 삽입
                if check(data): #성립하는지 확인
                    return True
                for r in range(m):
                    for c in range(m):
                        data[i + r][j + c] -= turn_key[r][c] # 키제거
    return False
