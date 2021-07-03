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

#     for name in participant:#참가자를 기록한다.
#         if dic.get(name) != None:#동명이인 체크
#             dic[name]+=1
#         else:
#             dic[name]=1
    
#     for name in completion:#완주한 사람 체크
#         dic[name]-=1

#     for name in participant:#완주하지 못한 사람 체크
#         if dic[name] != 0:
#             answer=name
#             break


#     return answer


participant=["leo", "kiki", "eden"]
completion=	["eden", "kiki"]

print(solution(participant,completion))