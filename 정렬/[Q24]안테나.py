#정렬한 다음 가운데 값을 찾으면 된다.
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(arr[len(arr)//2 - 1])
