n = int(input())

# 현재 못생긴 수에 2,3,5 곱한것이 또 못생긴 수가 된다.
i2 = i3 = i5 = 0 #2,3,5 곱 인덱스.
next2, next3, next5 = 2, 3, 5 #다음 2,3,5 곱한 값

dp = [0] * n
dp[0] = 1

for i in range(1, n):
    dp[i] = min(next2, next3, next5) #다음 2,3,5 곱한값의 최소값을 dp값으로.
    #선정시 인덱스 갱신. elif가 아닌 if를 사용함으로서 중복 방지가능.
    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5

print(dp[n-1])