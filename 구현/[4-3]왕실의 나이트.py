firstplace = input()
move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, 2), (-1, -2)]
yname = [0] + ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = int(firstplace[1])
y = int(yname.index(firstplace[0]))
print(x, y)

count = 0
for m in move:
    nx = x + m[0]
    ny = y + m[1]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1

print(count)