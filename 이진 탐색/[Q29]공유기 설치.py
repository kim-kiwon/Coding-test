#적정 gap을 mid로 하여 탐색.

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

min_gap = 1e9
for i in range(1, n):
    gap = arr[i] - arr[i-1]
    if gap < min_gap:
        min_gap = gap

start = min_gap #집 간의 최소 gap
end = arr[n-1] - arr[0] #집 간의 최대 gap
result = 0

while (start <= end):
    mid = (start + end) // 2 #gap을 중간으로.
    val = arr[0]
    count = 1
    for i in range(1, n): #mid를 gap으로 하여 공유기 설치해나감.
        if arr[i] >= val + mid:
            val = arr[i]
            count += 1
    if count >= c: #c개 이상 설치 가능.
        start = mid + 1 #답을 뒤쪽에서 찾자.
        result = mid #답 후보
    else: #c개 이상 설치 불가.
        end = mid - 1 #답을 앞쪽에서 찾자.

print(result)