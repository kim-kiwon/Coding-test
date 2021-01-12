from sys import stdin

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n = int(input())
havelist = list(map(int, stdin.readline().rstrip().split()))

m = int(input())
requestlist = list(map(int, stdin.readline().rstrip().split()))

for i in requestlist:
    result = binary_search(havelist, i, 0, n-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

