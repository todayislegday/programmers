import sys

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
    
# def solution(participant, completion):
#     answer = ''
#     dic=dict()

#     for name in participant:#�����ڸ� ����Ѵ�.
#         if dic.get(name) != None:#�������� üũ
#             dic[name]+=1
#         else:
#             dic[name]=1
    
#     for name in completion:#������ ��� üũ
#         dic[name]-=1

#     for name in participant:#�������� ���� ��� üũ
#         if dic[name] != 0:
#             answer=name
#             break


#     return answer


participant=["leo", "kiki", "eden"]
completion=	["eden", "kiki"]

print(solution(participant,completion))