n, m = map(int, input().split())
arr = list(map(int, input().split()))

# mid : 절단기 높이
start = 0
end = max(arr)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            total += (x-mid)
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(result)