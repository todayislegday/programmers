def solution(answers):
    answer = []
    
    person1=[1,2,3,4,5]# 각 사람들 반복되는 규칙이 있음 
    person2=[2,1,2,3,2,4,2,5]
    person3=[3,3,1,1,2,2,4,4,5,5]
    
    check=[0,0,0]

    for i in range(len(answers)):
        if person1[i%len(person1)]==answers[i]:
            check[0]+=1
        
        if person2[i%len(person2)]==answers[i]:
            check[1]+=1
        
        if person3[i%len(person3)]==answers[i]:
            check[2]+=1

    maxvalue=max(check)
    for i in range(len(check)):
        if maxvalue == check[i]:
            answer.append(i+1)

    return answer

answers=[[1,2,3,4,5,1],[1,3,2,4,2]]

for i in answers:
    print(solution(i))