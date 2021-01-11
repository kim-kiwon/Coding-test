n = int(input())

arr = []
for _ in range(n):
    data = input().split()
    arr.append((data[0], data[1]))

arr = sorted(arr, key = lambda x : x[1])

for i in range(len(arr)):
    print(arr[i][0], end = ' ')