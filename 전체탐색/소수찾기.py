import itertools as it

def solution(numbers):
    answer = 0
    end=10**len(numbers)
    memo=[False,False]+[True]*(end-2)#소수인지 아닌지를 메모,0과1은 소수가 아니므로 미리 false
    for i in range(2,end):#에라토스 테네스의체,범위 10^주어진 문자열 길이 까지
        if memo[i]:
            for j in range(2*i,end,i):
                memo[j]=False


    perlist=list()
    for i in range(1,len(numbers)+1):#모든 순열을 만들어낸다.
        perlist+=list(it.permutations(list(numbers),i))

    for i in range(len(perlist)):#ex) ('1','7')형태를 17로
        perlist[i]=int("".join(perlist[i]))
    
    for i in set(perlist):
        if memo[i]:
            answer+=1

    return answer



answers=["17","011"]

for i in answers:
    print(solution(i))