

def solution(n, lost, reserve):
    answer = 0
    lost.sort()#�տ����� ���� �׸��� ������ ������ �����°� �����ֱ� ���ؼ� lost�� �������� ���ĵ� ���¿��� �Ѵ�.

    count=[1 for i in range(0,n+2)]#�Ǿ� ����� ���ʿ��� ������ �ǵڻ���� �����ʿ��� ������ if ó�� ���� �ʱ� ���ؼ� �߰������� ������ �־���
                                    #�⺻������ �Ѱ��� ������ ���� 1 �ʱ�ȭ
    count[0]=0#���� �������� �ʴ� ���,���� ü���� 0��
    count[n+1]=0#���� �������� �ʴ� ���


    for i in range(len(lost)):#�Ҿ������� ������¿��� -1
        count[lost[i]]-=1
    for i in range(len(reserve)):#�����λ�� ���� ���׿��� +1 ,���� ���·� �� ���� ������ �տ��� �о� ���� ����� ������ ����� ��� 
        count[reserve[i]]+=1       #���� ���°� �ʿ��ϱ� ����

    for i in range(len(lost)):
        if count[lost[i]-1] == 2: #�Ҿ���� ����� �տ��� ���� ���ʿ��� ������
            count[lost[i]-1]-=1
            count[lost[i]]=1
            continue
        
        if count[lost[i]+1] == 2:#���ʿ��� �������� �����ʿ��� ������
            count[lost[i]+1]-=1
            count[lost[i]]=1
            continue

    for i in range(1,len(count)-1):#������ ����� üũ
        if count[i] == 0:
            answer-=1
    answer+=n #��ü �ο��� ������ ����� ���ش�.

    return answer





n=3
lost=[3]
reserve=[1]

print(solution(n,lost,reserve))