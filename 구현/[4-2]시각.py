N = int(input())

count = 0

def check(a):
    if a % 10 == 3 or (a>= 30 and a<40):
        return True

for i in range(0, N+1):
    for j in range(0, 60):
        for k in range(0, 60):
            if check(i) or check(j) or check(k):
                count += 1

print(count)