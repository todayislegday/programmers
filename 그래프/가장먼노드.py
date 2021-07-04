from collections import deque

def solution(n, edge):
    answer = 0
    
    node={}#인접리스트 표현

    for i in range(1,n+1):
        node[i]=list()

    for i in edge:
        f=i[0]
        t=i[1]
        node[f].append(t)#양방향
        node[t].append(f)
            
    queue=deque([(1,0)])#시작 노드 인덱스,가중치의 합
    visited={1}
    count=[0 for i in range(n+1)]#1번부터 해당 노드까지의 가중치의 합


    while queue:
        findex,cvalue=queue.pop()
        for tindex in node[findex]:
            if tindex not in visited:# 가려는 곳이 방문 하지 않았다면
                visited.add(tindex)#방문 체크
                queue.appendleft((tindex,cvalue+1))
                count[tindex]=cvalue+1

    mvalue=max(count)#1부터 특정 노드 까지의 가중치 합이 최대인 값을 구함
    answer=count.count(mvalue)#가중치 합이 최대에 해당하는 노드 개수

    return answer


n=6
vertex=	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,vertex))