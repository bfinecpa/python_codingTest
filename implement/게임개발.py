N, M = map(int, input().split())

curA, curB, d = map(int ,input().split())

map = [list(map(int, input().split())) for _ in range(M)]

map[curA][curB]=2

moveA = [-1, 0, 1, 0]
moveB = [0, 1, 0, -1]

count = 1

while(True):
    dCount=0
    for _ in range(4):
        
        d-=1
        if(d==-1):
            d=3

        if (map[curA+moveA[d]][curB+moveB[d]]==0):
            curA += moveA[d]
            curB += moveB[d]
            map[curA][curB]=2
            count+=1
            break
        else:
            dCount+=1
            continue

    if(dCount==4):
        if d==0:
            if(map[curA+moveA[2]][curB+moveB[2]]==1):
                break
            else:
                curA += moveA[2]
                curB += moveB[2]
        if d==1:
            if(map[curA+moveA[3]][curB+moveB[3]]==1):
                break
            else:
                curA += moveA[3]
                curB += moveB[3]
        if d==2:
            if(map[curA+moveA[0]][curB+moveB[0]]==1):
                break
            else:
                curA += moveA[0]
                curB += moveB[0]
        if d==3:
            if(map[curA+moveA[1]][curB+moveB[1]]==1):
                break
            else:
                curA += moveA[1]
                curB += moveB[1]

print(count)