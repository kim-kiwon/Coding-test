n, k = map(int ,input().split())

result = 0
while 1:
    target = (n//k) * k #k로 나누어떨어지는 수 중 가장 n에 가까운 수
    result += (n - target)
    n = target
    if n < k:
        break
    n //= k
    result += 1

result += (n-1)
print(result)