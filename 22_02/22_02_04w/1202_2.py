# 보석 도둑 ( 시간초과 )

import sys
import heapq
from collections import deque

# n: 보석개수 k: 가방개수
n,k = map(int,sys.stdin.readline().split())

arr = []

for i in range(n):
    m,v = map(int,sys.stdin.readline().split())
    heapq.heappush(arr,(-v,m))


b = [int(sys.stdin.readline()) for _ in range(k)]
b.sort()
queue = deque()
for i in range(k):
    queue.append(b[i])

answer = 0
is_pop = False

while queue:
    is_pop = False

    for i in range(len(queue)):
        if queue[-1]<arr[0][1]:
            break

        if arr[0][1]<=queue[i]:
            answer += -arr[0][0]
            heapq.heappop(arr)
            queue.popleft()
            is_pop = True
            break
        else:
            continue
    
    
    if is_pop:
        continue    
    else:
        heapq.heappop(arr)
        
print(answer)