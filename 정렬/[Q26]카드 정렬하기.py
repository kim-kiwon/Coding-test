#최소 값 문제 -> min heap 사용하자

import heapq

#최소 값 두 뭉치를 선택 해나가면 답 도출 가능.
n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))

result = 0
while True:
    if len(arr) == 1:
        break
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    result += (a+b)
    heapq.heappush(arr, a + b)

print(result)