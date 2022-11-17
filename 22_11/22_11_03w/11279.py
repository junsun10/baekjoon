# 최대 힙 ( 정답 )
# 알고리즘 : heap
# 최대 힙을 만들기 위해 입력값에 -를 붙여 저장

import sys
import heapq

n = int(sys.stdin.readline())
heap = []
heapq.heapify(heap)

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, [-x, x])
