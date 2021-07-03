import sys
from collections import deque#데크 자료구조를 bfs를 위해 큐처럼 사용

def solution(numbers, target):
    answer = 0
    queue=deque([(0, 0)])#누적값,현재 인덱스

    while queue:
        nowvalue,nowindex=queue.pop()

        if nowindex == len(numbers):
            if nowvalue == target:
                answer+=1
        else:
            queue.appendleft((nowvalue+numbers[nowindex],nowindex+1))
            queue.appendleft((nowvalue-numbers[nowindex],nowindex+1))
    return answer

# def solution(numbers, target):
#     answer = 0
#     answer=dfs(numbers,0,0,target)
#     return answer

# def dfs(numbers,index,nowvalue,target):
#     if index==len(numbers):#numbers의 끝까지 연산
#         if nowvalue == target:#연산한 값이 원하는 값이라면
#             return 1#방법 1가지를 return 하여 더해줌
#         return 0#끝까지 연산했지만 원하는 값이 아니므로 방법이 아닌 경우의수 따라서 0 return

#     ans=0
#     ans+=dfs(numbers,index+1,nowvalue+numbers[index],target)
#     ans+=dfs(numbers,index+1,nowvalue-numbers[index],target)

#     return ans    


numbers=[1, 1, 1, 1, 1]
target=3

print(solution(numbers,target))