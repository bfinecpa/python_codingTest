S = list(input())
alpha = []
num = []

for i in S:
    if ord(i)>= ord('A') and ord(i)<=ord('Z'):
        alpha.append(i)
    else:
        num.append(int(i))

alpha.sort()
valSum = sum(num)

print(*alpha,valSum, sep="")
