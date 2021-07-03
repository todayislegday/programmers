import sys

def solution(prices):
    answer = [0 for i in range(len(prices))]
    stack=[] #스택에[값,인덱스]형식으로 넣어준다.
    for i in range(0,len(prices)):
       
        while stack:#스택에 값이 존재하는동안 계속  맨위 비교
            if prices[i]<stack[-1][0]:#스택 맨위의 값이 더 크고 다음에 넣을께 작다면.. 가격이 떨어진 것,떨어진 부분까지 체크 
                answer[stack[-1][1]]=i-stack[-1][1]
                stack.pop()
            else:#떨어지지않은게 맨위면 탈출
                break

        stack.append([prices[i],i])#스택맨위에 넣어준다.
               
    
    lastindex=len(prices)-1
    while stack: #비어있지 않으면 True
        temp=stack.pop()[1]#인덱스만 필요있음
        answer[temp]=lastindex-temp

    return answer   
    


prices=[1,2,3,2,3]
print(solution(prices))