import sys

def solution(array, commands):
    answer = []

    for command in commands:
        s,e,index=command

        temp=array[s-1:e]#자르고
        temp.sort()#정렬하고
        answer.append(temp[index-1])


    return answer



array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array,commands))