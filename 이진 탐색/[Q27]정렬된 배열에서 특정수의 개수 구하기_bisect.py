#bisect_left : 정렬된 상태에서 arr에 x를 삽입할 때 최소 인덱스 반환.
#bisect_right : 위의 상황에서 최대 인덱스를 반환.
#정렬된 리스트에서 특정 범위 원소의 개수를 파악할때 사용.

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

arr = list(map(int, input().split()))

left = bisect_left(arr, x)
right = bisect_right(arr, x)

if right - left != 0:
    print(right - left)
else:
    print(-1)