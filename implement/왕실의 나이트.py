curlocation = list(input())

##  문자를 ascii 숫자로 바꾸려면 ord()를 사용하자 숫자인 문자는 무조건 int
x=ord(curlocation[0])
y=int(curlocation[1])

move_x = [-2, -2, -1, -1, 1, 1, 2, 2]
move_y = [-1,  1,  2, -2, 2, -2, 1, -1]

count =0

for i in range(8):
    curx= x+move_x[i]
    cury= y+move_y[i]
    if curx<=104 and curx>=97:
        if cury<=8 and cury >=1:
            count+=1
print(count)


