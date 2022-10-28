# 가운데를 말해요 ( 정답 )
# 가운데보다 작으면 왼쪽힙, 크면 오른쪽힙에 넣음
# 왼쪽힙 루트가 오른쪽힙 루트보다 크면 서로바꿈
# 왼쪽힙은 최대힙, 오른쪽힙은 최소힙
# 서로개수가 같으면 왼쪽힙에 다르면 오른쪽힙에 넣음


import sys
import heapq

# N 입력
n = int(sys.stdin.readline())

left_heap = []
right_heap = []

for i in range(n):
    temp = int(sys.stdin.readline())
    if len(left_heap)==len(right_heap):
        heapq.heappush(left_heap,(-temp,temp))
    else:
        heapq.heappush(right_heap,(temp,temp))
    
    if len(right_heap)!=0 and left_heap[0][1]>right_heap[0][1]:
        x = heapq.heappop(right_heap)[0]
        y = heapq.heappop(left_heap)[1]
        heapq.heappush(right_heap,(y,y))
        heapq.heappush(left_heap,(-x,x))

    print(left_heap[0][1])
