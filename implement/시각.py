#완전탐색은 100만개 이하일때 사용하면 적절하다.

N= int(input())

if N>=3:
    no3=(N)*15*105
    rest = 60*60
    print(no3+rest)
elif N<3:
    print((N+1)*15*105)
