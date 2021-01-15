n = input()

length = len(n)

leftsum = rightsum = 0

for i in n[:length//2]:
    leftsum += int(i)

for i in n[length//2:]:
    rightsum += int(i)

if leftsum == rightsum:
    print("LUCKY")
else:
    print("READY")