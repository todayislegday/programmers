
def solution(citations):
    answer = 0

    citations.sort(reverse=True)

    for i,citation in enumerate(citations):
        if i+1==citation:
            answer=citation
            break

    return answer


citations=[3, 0, 6, 1, 5]
print(solution(citations))