from sys import stdin

n = int(stdin.readline())
array = [0] * 1000001

for i in stdin.readline().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, stdin.readline().split()))

for i in x:
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')