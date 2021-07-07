import sys
"""
from itertools import permutations
def solution(numbers):
    answer = ''
    slist=list(map(str,numbers))
    slist.sort(key = lambda x: x*3,reverse=True)

    if slist[0] == '0':#가장 큰값이 0이면 전부다 0 
        return '0'
    else:
        return ''.join(slist)

    return answer
"""
import functools

def comparator(a,b):#내림 차순 정렬
    t1 = a+b
    t2 = b+a
    return int(t2)-int(t1) #양수 리턴 b,a 변경

def solution(numbers):
    n = list(map(str,numbers))
    n = sorted(n, key=functools.cmp_to_key(comparator))
    answer = str(int(''.join(n)))
    return answer

numbers=[[6, 10, 2],[3, 30, 34, 5, 9]]

for i in numbers:
    print(solution(i))