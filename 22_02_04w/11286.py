# 절댓값 힙 ( 정답 )
# 양수와 음수를 각각의 힙에 저장

import sys
import heapq

n = int(sys.stdin.readline())

plus_heap = []
minus_heap = []

for _ in range(n):
    input_value = int(sys.stdin.readline())

    # 출력
    if input_value == 0:
        if len(plus_heap) == 0 and len(minus_heap) == 0:
            print(0)
        elif len(plus_heap) == 0 and len(minus_heap) != 0:
            print(-heapq.heappop(minus_heap))
        elif len(minus_heap) == 0 and len(plus_heap) != 0:
            print(heapq.heappop(plus_heap))
        else:
            if plus_heap[0] == minus_heap[0]:
                print(-heapq.heappop(minus_heap))
            elif plus_heap[0] < minus_heap[0]:
                print(heapq.heappop(plus_heap))
            else:
                print(-heapq.heappop(minus_heap))

    # 저장
    elif input_value > 0:
        heapq.heappush(plus_heap,input_value)
    elif input_value < 0:
        heapq.heappush(minus_heap,-input_value)
    
       