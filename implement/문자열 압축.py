def solution(s):
    # answer=len(s)
    # for i in range(1, len(s)//2+1):
    #     curList= []
    #     curSlice = i
    #     for i in range(len(s)//curSlice):
    #         curIdx=i*curSlice
    #         curList.append(s[curIdx:curIdx+curSlice])
    #         if(i==(len(s)//curSlice)-1):
    #             if(len(s)%curSlice!=0):
    #                 curList.append(s[curIdx+curSlice:])


    length = len(s)
    answer = length
    for i in range(1, length//2+1):
        curLength = 0
        valCount = 0
        preVal = ''
        curVal = ''
        for j in range(0, length, i):
            curVal = s[j:j+i]
            if(curVal==preVal):
                preValCount = valCount
                valCount+=1
                if(valCount>2):
                    if(len(str(preValCount))<len(str(valCount))):
                        curLength+=1
                else:
                    curLength+=1
            else:
                curLength+=len(curVal)
                preVal=curVal
                valCount=1
        if answer>curLength:
            answer=curLength

    return answer

            
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("aaaaaaaaaabbbbbbbbbb"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))

### 리스트 -> 문자열 : join

### 구현의 대한 생각
### 우선 문제 파악을 정확하게 하고, 구현을 하는데, 조건이 필요하면 변수를 설정해서 빠르게 구현하자.

