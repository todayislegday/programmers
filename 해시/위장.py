import sys
def solution(clothes):
    answer = 1
    dicclothes=dict()
    for cloth in clothes:
        if  cloth[1] not in dicclothes:
            dicclothes[cloth[1]]=list()
            dicclothes[cloth[1]].append(cloth[0])
        else:     
            dicclothes[cloth[1]].append(cloth[0])
    
    for clothtype in dicclothes:
        dicclothes[clothtype].append("") #종류에서 아무것도 안골름

    for clothtype in dicclothes:
        answer*=len(dicclothes[clothtype])
    return answer-1#아무것도 고르지 않은 경우만 제외

clothes=[[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]],[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]]

for i in clothes:
    print(solution(i))