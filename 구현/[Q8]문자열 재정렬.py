s = input()

alphabet = []
num = []

for i in s:
    if i.isalpha():
        alphabet.append(i)
    elif i.isnumeric():
        num.append(int(i))

alphabet = sorted(alphabet)
summ = sum(num)

for i in alphabet:
    print(i, end = "")

print(summ)