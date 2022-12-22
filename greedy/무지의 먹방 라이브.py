# 매우매우매우매우 중요 중요 중요 중요 ############################################################
# 그리드에 대한 나의 생각
# 현재에서 가장 최적인 값을 선택해야 하므로 
# 바로 최적이 생각이 안나면 최소, 최대를 생각해야 한다.
import heapq

def solution(food_times, k):

    if sum(food_times)<=k:
        return -1
    
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i], i+1))

    sum_value = 0
    previous = 0

    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -=1
        previous = now
    
    result = sorted(q, key= lambda x: x[1])
    return result[(k-sum_value) % length][1]

print(solution([3,1,2],5))