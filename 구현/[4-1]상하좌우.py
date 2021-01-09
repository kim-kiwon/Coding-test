n = int(input())
x, y = 1, 1
move = input().split()

def canmove(a, b):
    if a >= 1 and a <= n and b >= 1 and b <= n:
        return True

for i in move:
    if i == 'L' and canmove(x, y-1):
        y -= 1
    elif i == 'R' and canmove(x, y+1):
        y += 1
    elif i == 'U' and canmove(x-1, y):
        x -= 1
    elif i == 'D' and canmove(x+1, y):
        x += 1

print(x, y)