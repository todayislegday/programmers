import sys
from collections import deque
def solution(n, computers):
    answer = 0
    computernode=dict()
    visited=set()

    for i in range(len(computers)):
        computernode[i]=list()
        for j in range(len(computers)):
            if i==j:
                continue
            if computers[i][j]==1:
                computernode[i].append(j)


    for i in range(len(computers)):
        if i not in visited:#방문 하지 않은 노드라면
            que=deque([i])#출발노드
            visited.add(i)
            answer+=1
            while que:#탐색 시작
                f=que.pop()
                for t in computernode[f]:
                    if t not in visited:
                        que.appendleft(t)
                        visited.add(t)


    return answer


n=[3,3]
computers=[[[1, 1, 0], [1, 1, 0], [0, 0, 1]],[[1, 1, 0], [1, 1, 1], [0, 1, 1]]]

for a,b in zip(n,computers):
    print(solution(a,b))