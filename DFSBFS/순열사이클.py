import sys

def DFS(now,perlist,visited):
    
    if now not in visited:
        visited.add(now)
        DFS(perlist[now],perlist,visited)

    return 1


T=int(input())


while T>0:
    T-=1

    N=int(input())
    perlist=list(map(int,sys.stdin.readline().split()))
    perlist.insert(0,0)#편하게 숫자랑 인덱스 맞추기 위해서 앞에 0넣기
    visited=set()

    ans=0
    for i in range(1,N+1):
        if i not in visited:
            visited.add(i)
            ans+=DFS(perlist[i],perlist,visited)


    print(ans)
    
