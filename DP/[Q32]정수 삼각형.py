#DP로 각 피라미드 위치에서 최대값을 저장하자.
#양쪽 사이드는 선택할 수 있는 것이 하나뿐.
n = int(input())
arr = [0] * n

for i in range(n):
    arr[i] = list(map(int, input().split()))

for i in range(1, n):
    arr[i][0] = arr[i][0] + arr[i-1][0]
    arr[i][i] = arr[i][i] + arr[i-1][i-1]
    for j in range(1, i):
        arr[i][j] = arr[i][j] + max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[n-1]))