a = input()
b = input()

n = len(a)
m = len(b)

arr = [[0] * (m+1) for _ in range(n+1)]

#dp 배열 초기화
for i in range(m+1):
    arr[0][i] = i
for i in range(n+1):
    arr[i][0] = i

#dp 이용 나머지 칸 도출
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]: #목표 문자열과 현재 단어가 같다면.
            arr[i][j] = arr[i-1][j-1] #대각선 값 그대로
        else: #다르다면
            arr[i][j] = min(arr[i - 1][j - 1], arr[i - 1][j], arr[i][j - 1]) + 1 #대각선/위/왼쪽 중 최소값 + 수정비용.
print(arr[n][m])