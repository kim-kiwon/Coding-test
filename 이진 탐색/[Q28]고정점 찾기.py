#정렬된 배열에서의 탐색. 이진탐색을 활용한다.
n = int(input())
arr = list(map(int, input().split()))

start = 0
end = len(arr) - 1
find = 0
while start <= end:
    mid = (start + end) // 2
    if arr[mid] == mid:
        find = 1
        print(mid)
        break
    elif arr[mid] > mid: #미드의 배열 값이 인덱스보다 크면. 인덱스와 값이 같은놈은 앞쪽에 존재. end를 당긴다.
        end = mid - 1
    else:
        start = mid + 1 #반대의 경우. start를 뒤로 민다.

if find == 0:
    print(-1)
