#값 받기
n,m,k = map(int, input().split())

#값 리스트로 받기
n_list = list(map(int, input().split()))

n_list.sort()


r = m%(k+1)
q = m//(k+1)

print((k*n_list[-1]+n_list[-2])*q+(r*n_list[-1]))