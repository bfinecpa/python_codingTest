data = list(map(int, input()))

zeroCount = 0
oneCount =0

for i in range(len(data)):
    if i==0:
        if data[i]==1:
            oneCount+=1
        else:
            zeroCount+=1
    else:
        if data[i] ==1 and data[i-1]==0:
            oneCount+=1
        elif data[i]==0 and data[i-1]==1:
            zeroCount+=1

print(min(zeroCount,oneCount))