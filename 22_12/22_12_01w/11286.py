# 절댓값 힙 ( 정답 )
# 알고리즘 : 힙
# 절댓값이 작은 순으로 정렬하기 위해 원형과 절댓값 모두 저장

from heapq import *
import sys

heap = []


for _ in range(int(input())):
    i = int(sys.stdin.readline())
    if i == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap)[1])
    elif i < 0:
        heappush(heap, (-i, i))
    else:
        heappush(heap, (i, i))
