# 최소 힙 ( 정답 )
# 알고리즘 : heap
# heap의 사용
# 입력을 sys를 사용해 시간초과 해결

import heapq
import sys

heap = []
heapq.heapify(heap)

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
