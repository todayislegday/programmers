from collections import deque

def solution(n, results):
    answer = 0
    windict=dict()#노드(나) 기준으로 부터 나를 이긴 노드들
    losedict=dict()#노드(나) 기준으로 부터 나한테 진 노드들
   
    count=[0 for i in range(n+1)]
    for result in results:
        if result[1] not in windict:
            windict[result[1]]=[]
        if result[0] not in losedict:
            losedict[result[0]]=[]
        
        windict[result[1]].append(result[0])
        losedict[result[0]].append(result[1])

    
    for i in range(1,n+1):#노드 기준으로 탐색
        visited=set()
        que=deque([i])
        visited.add(i)
        while que:#windict 사용
            f=que.pop()
            if f in windict:
                for t in windict[f]:
                    if t not in visited:
                        visited.add(t)
                        que.appendleft(t)
                        count[i]+=1
                

        visited=set()
        que=deque([i])
        visited.add(i)
        while que:#losedict 사용
              f=que.pop()
              if f in losedict:
                for t in losedict[f]:
                    if t not in visited:
                        visited.add(t)
                        que.appendleft(t)
                        count[i]+=1

    answer=count.count(n-1)


    return answer

n=5
results=[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

print(solution(n,results))

