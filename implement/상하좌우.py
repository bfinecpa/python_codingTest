N = int(input())

data = list(input().split(" "))

curLocation = [1,1]

for i in data:
    if i == "L":
        if curLocation[1]!=1:
            curLocation[1]-=1
    elif i == "R":
        if curLocation[1]!=N:
            curLocation[1]+=1
    elif i == "U":
        if curLocation[0]!=1:
            curLocation[0]-=1
    elif i == "D":
        if curLocation[0]!=N:
            curLocation[0]+=1

print(curLocation[0],curLocation[1])