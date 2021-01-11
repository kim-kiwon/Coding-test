n, m, k = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort(reverse=True)

first = nums[0]
second = nums[1]

result = 0
while 1:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1


print(result)