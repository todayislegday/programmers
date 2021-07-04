

def solution(n, lost, reserve):
    answer = 0
    lost.sort()#앞에부터 왼쪽 그리고 오른쪽 순서로 빌리는걸 지켜주기 위해서 lost는 오름차순 정렬된 상태여야 한다.

    count=[1 for i in range(0,n+2)]#맨앞 사람이 왼쪽에서 빌릴때 맨뒤사람이 오른쪽에서 빌릴때 if 처리 하지 않기 위해서 추가적으로 여분을 넣어줌
                                    #기본적으로 한개씩 가지고 있음 1 초기화
    count[0]=0#실제 존재하지 않는 사람,따라서 체육복 0개
    count[n+1]=0#실제 존재하지 않는 사람


    for i in range(len(lost)):#잃어버린사람 현재상태에서 -1
        count[lost[i]]-=1
    for i in range(len(reserve)):#여분인사람 현재 상테에서 +1 ,현재 상태로 써 놓은 이유는 앞에서 읽어 버린 사람이 여분인 사람일 경우 
        count[reserve[i]]+=1       #현재 상태가 필요하기 때문

    for i in range(len(lost)):
        if count[lost[i]-1] == 2: #잃어버린 사람중 앞에서 부터 왼쪽에서 빌린다
            count[lost[i]-1]-=1
            count[lost[i]]=1
            continue
        
        if count[lost[i]+1] == 2:#왼쪽에서 못빌리면 오른쪽에서 빌린다
            count[lost[i]+1]-=1
            count[lost[i]]=1
            continue

    for i in range(1,len(count)-1):#못빌린 사람을 체크
        if count[i] == 0:
            answer-=1
    answer+=n #전체 인원중 못빌린 사람을 빼준다.

    return answer





n=3
lost=[3]
reserve=[1]

print(solution(n,lost,reserve))