# DP로 i번째 날에 최대 수익을 계산하자.
n = int(input())
t = []
p = []
dp = [0] * (n+1)

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

maxval = 0
for i in range(n-1, -1, -1):
    time = i + t[i]
    if time <= n:
        dp[i] = max(maxval, p[i]+dp[i + t[i]])
        maxval = dp[i]
    else:
        dp[i] = maxval

print(maxval)