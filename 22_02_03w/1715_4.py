# 카드 정렬하기 ( 정답 )

import sys
import heapq

# N 입력
n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    heapq.heappush(heap,int(sys.stdin.readline()))

answer = 0

if len(heap)==1:
    print(0)
else:
    while True:
        temp = 0
        temp += heapq.heappop(heap)
        temp += heapq.heappop(heap)

        answer += temp
        heapq.heappush(heap,temp)

        if len(heap)==1:
            break
    print(answer)
