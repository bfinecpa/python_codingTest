s = list(input())

data = list(map(int, s))

v= 0
for i in data:
    if i==0 or i ==1:
        v=v+i
    else:
        if v==0:
            v+=i
        else:
            v*=i
print(v)