import heapq

def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap: #heap에 빼낼게 있을때만 작동 한다고 했다.
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]

# import heapq

# def solution(operations):
#     answer = []
#     minheap=[]
#     maxheap=[]

#     for operation in operations:
#         a,b=operation.split()
#         b=int(b)
#         if a=="I":
#             heapq.heappush(minheap,b)
#             heapq.heappush(maxheap,(-b,b))
#         else:
#             if len(minheap)==0:
#                 continue
#             if b==1:
#                 heapq.heappop(maxheap)
#                 minheap=heapq.nsmallest(len(maxheap),minheap)
#             else:
#                 heapq.heappop(minheap)
#                 maxheap=heapq.nsmallest(len(minheap),maxheap)
    
#     if not minheap:
#         return [0,0]
#     else:
#         return [max(minheap),min(minheap)]


operations=[["I 16","D 1"],["I 7","I 5","I -5","D -1"],["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"],["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]]
for i in operations:
    print(solution(i))