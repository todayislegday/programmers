def solution(triangle):
    answer = 0
    dp=[[0 for i in range(len(triangle))] for j in range(len(triangle)) ]#���⼭�� �簢������ �ص� �������,,�ﰢ������ �ص� �� �������
    dp[0][0]=triangle[0][0]

    for i in range(len(triangle)-1):#���������� �������� �ִ��� ���ϴ°����� �������� ���� ������
         for j in range(len(triangle[i])):
            if dp[i+1][j]<dp[i][j]+triangle[i+1][j]:#�������� ��������
                dp[i+1][j]=dp[i][j]+triangle[i+1][j]
            if dp[i+1][j+1]<dp[i][j]+triangle[i+1][j+1]:#���������� ��������
                dp[i+1][j+1]=dp[i][j]+triangle[i+1][j+1]
        
    for value in dp[len(triangle)-1]:#���������� �ִ񰪵��� �����Ƿ� ���߿��� ���� ���� �ִ����� ���Ѵ�.
        if answer<value:
            answer=value
    return answer


tr=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(tr))