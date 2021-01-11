n, m = map(int, input().split())
arr = []
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(min(temp))

print(max(arr))