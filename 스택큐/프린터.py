import sys

def solution(priorities, location):
    answer = 0
    indexing=[0 for i in range(len(priorities))]
    sum=1
    indexing[location]=1


    while max(indexing) == 1:
        if max(priorities) == priorities[0]:
            priorities.pop(0)
            sum-=indexing.pop(0)
            answer+=1
        else:
            priorities.append(priorities.pop(0))
            indexing.append(indexing.pop(0))
    return answer



priorities=[[2, 1, 3, 2],[1, 1, 9, 1, 1, 1]]
location=[2,0]
for i,j in zip(priorities,location):
    print(solution(i,j))