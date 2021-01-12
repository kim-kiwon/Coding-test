n, m = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [999999999] * (m+1)
dp[0] = 0

for i in range(min(coins), m+1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[m] == 999999999:
    print(-1)
else:
    print(dp[m])
