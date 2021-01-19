s = input()
dp = [0] * len(s)

dp[0] = int(s[0])

for i in range(1, len(s)):
    first = dp[i-1]
    second = int(s[i])

    dp[i] = max(first + second, first * second)

print(dp[len(s)-1])