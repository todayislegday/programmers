def solution(citations):
    
    citations.sort(reverse=True)
    l=len(citations)
    answer=l
    for i in range(l):
        if citations[i] <=i:
            return i
    return answer

citations=[[4,0,5],[3, 0, 6, 1, 5],[88,89],[0,0,0,0]]
for i in citations:
    print(solution(i))