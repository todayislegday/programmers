import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    
    while scoville:#or True
        if scoville[0]>=K:#가장 작은 값이 k이상이면
            return answer
        
        if len(scoville)==1:#한개 남았다면 아래 행위 불가능
            break

        answer+=1
        low1=heapq.heappop(scoville)
        low2=heapq.heappop(scoville)

        newvalue=low1+(low2*2)
        heapq.heappush(scoville,newvalue) #새로운 값을 넣어준다.
      
    return -1


s = [[1,2,3,9,10,12], [0, 0], [1,2], [1,2,3], [7, 1], [3, 4], [4, 4], [3, 3], [1,5], [2,3,7,10,15]]
k = 7
for i in s:
    print(solution(i, k))