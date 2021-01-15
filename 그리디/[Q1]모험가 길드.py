n = int(input())

arr = list(map(int, input().split()))

arr.sort()

result = 0
temp = []

for i in range(0, len(arr)):
    temp.append(arr[i])
    if max(temp) <= len(temp):
        result += 1
        temp = []

print(result)