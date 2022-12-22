N = list(map(int, input()))

size =len(N)

leftList = N[:size//2]
rightList = N[size//2:]
if(sum(leftList) == sum(rightList)):
    print("LUCKY")
else:
    print("READY")
