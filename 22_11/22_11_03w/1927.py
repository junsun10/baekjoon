# 최소 힙 ( 시간초과 )
# 알고리즘 : heap
# 입력을 input으로 받아서 시간초과

import heapq

heap = []
heapq.heapify(heap)

n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
