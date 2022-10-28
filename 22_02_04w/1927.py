# 최소 힙 ( 정답 )

import sys
import heapq

n = int(sys.stdin.readline())

min_heap = []

for _ in range(n):
    input_value = int(sys.stdin.readline())

    if input_value == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap,input_value)