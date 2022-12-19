n = int(input())

data = list(map(int, input().split()))

data.sort()

cur = 0
count =0
while(True):
    if(cur+data[cur]>=n):
        break
    cur=cur+data[cur]
    count +=1
print(count)
