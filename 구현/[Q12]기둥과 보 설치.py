build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1],[1,0,0,0]]
n = 5

# 건물에 해당 부품이 배치 가능한가.
def can(x, y, a, ans):
    if a == 0: #기둥
        if y == 0 or [x-1, y, 1] in ans or [x, y, 1] in ans or [x, y-1, 0] in ans: #바닥 or 다른기둥 위 or 보 오른쪽 위 or 보 왼쪽 위
            return True
        return False
    else: #보
        if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans or ([x-1, y, 1] in ans and [x+1, y, 1] in ans): #왼쪽 아래 기둥 or 오른쪽 아래 기둥 or 보 사이
            return True
        return False

def solution(n, build_frame):
    answer = []
    for data in build_frame:
        x, y, a, b = data
        if b == 1: #부품 추가
            if can(x, y, a, answer):
                answer.append([x, y, a])
        else: #부품 삭제
            answer.remove([x, y, a]) #먼저 삭제하고
            for val in answer: #현재 건물들 부품 돌면서 규칙 깨진 부품 있나 확인.
                nx, ny, na = val
                if can(nx, ny, na, answer) == True:
                    continue
                else: #있으면 삭제한 부품 다시 추가
                    answer.append([x, y, a])
                    break
    answer.sort(key = lambda x : (x[0], x[1], x[2]))
    return answer

print(solution(5, build_frame))