n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = arr[1]
dp[2] = max(arr[1], arr[2])
for i in range(3, n+1):
    dp[i] = max(arr[i]+dp[i-2], dp[i-1])

print(dp[n])
