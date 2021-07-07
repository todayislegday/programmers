def solution(n, times):
    answer = 0
    left=0
    right=2*max(times)*n #가장 시간이 오래걸리는 심사관한테만 전부 받을때 시간이 가장 많이 걸림,*2는 mid기준으로 구하기 때문에 

    while left<=right:
        mid=(left+right)//2
        sum=0
        for time in times:
            sum=sum+mid//time
            
        if sum>=n:
            right=mid-1
            answer=mid
        else:
            left=mid+1
            
    return answer

n=6
times=[7,10]
print(solution(n,times))