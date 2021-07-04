def solution(triangle):
    answer = 0
    dp=[[0 for i in range(len(triangle))] for j in range(len(triangle)) ]#여기서는 사각형으로 해도 상관없고,,삼각형으로 해도 별 상관없다
    dp[0][0]=triangle[0][0]

    for i in range(len(triangle)-1):#현재층으로 다음층의 최댓값을 구하는것으로 마지막층 전층 까지만
         for j in range(len(triangle[i])):
            if dp[i+1][j]<dp[i][j]+triangle[i+1][j]:#왼쪽으로 내려갈때
                dp[i+1][j]=dp[i][j]+triangle[i+1][j]
            if dp[i+1][j+1]<dp[i][j]+triangle[i+1][j+1]:#오른쪽으로 내려갈때
                dp[i+1][j+1]=dp[i][j]+triangle[i+1][j+1]
        
    for value in dp[len(triangle)-1]:#마지막층에 최댓값들이 있으므로 그중에서 뭐가 제일 최댓값인지 구한다.
        if answer<value:
            answer=value
    return answer


tr=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(tr))