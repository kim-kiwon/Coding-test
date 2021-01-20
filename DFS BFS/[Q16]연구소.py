#백트래킹 + DFS.
#최대 8x8로 배열크기 제한 -> 백트래킹 완전탐색 가능.
#바이러스 전파시키는 dfs 구현. -> arr를 복사한 새로운 배열에서 수행.
#안전 영역 크기 확인하는 완전 탐색 구현. -> arr를 복사한 새로운 배열에서 수행.
#벽 세개 세우는 백트래킹 방식 구현. -> arr에서 수행할것.
import copy
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
checkarr = copy.deepcopy(arr)

def virus(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if checkarr[x][y] == 0 or checkarr[x][y] == 2:
        checkarr[x][y] = 3
        virus(x-1 , y)
        virus(x+1, y)
        virus(x, y-1)
        virus(x, y+1)
    return

def getscore(arr):
    score = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                score += 1
    return score

result = -int(1e9)
def backtracking(count, r):
    global checkarr, result
    if count == 3:
        checkarr = copy.deepcopy(arr)
        for i in range(n):
            for j in range(m):
                if checkarr[i][j] == 2:
                    virus(i, j)
        result = max(result, getscore(checkarr))
        return
    for i in range(r, n):
        for j in range(m):
            if arr[i][j] == 0 :
                arr[i][j] = 1
                backtracking(count + 1, i)
                arr[i][j] = 0

backtracking(0, 0)
print(result)
