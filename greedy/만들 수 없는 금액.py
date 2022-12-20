n = int(input())

data = list(map(int, input().split(" ")))

data.sort()

#1 1 2 3 9
sumV = sum(data)
#[1 2 3 4 5 6 ]
maxV = 0

dataTable = [0] * (sumV+2)
dataTable[0]=1
for i in data:
    for j in range(maxV+1):
        if dataTable[j]==1:
            dataTable[j+i]=1
            maxV = j+i
        
for i in range(sumV+2):
    if(dataTable[i] == 0):
        print(i)
        break

