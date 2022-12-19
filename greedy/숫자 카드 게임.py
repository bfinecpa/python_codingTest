n, m = map(int, input().split())

#2중 배열 받기
data = [list(map(int, input().split())) for _ in range(n)]

s=0

for i in range(n):
    m = min(data[i])
    if s<m:
        s=m
print(s)

#최솟값은 min으로 구할 수 있다.

