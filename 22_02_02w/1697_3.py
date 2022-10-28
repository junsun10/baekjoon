# 숨바꼭질 ( 시간초과 )
# 방문안한값만 큐에 더함


import sys
from collections import deque

# N,K 입력
n,k = map(int,sys.stdin.readline().split())

visited = []
queue = deque()
queue.append((n,0))

if n==k:
    print(0)
else:
    while True:
        popvalue, second = queue.popleft()
        if popvalue+1 == k or popvalue-1 == k or popvalue*2 == k:
            print(second + 1)
            break
        else:
            if popvalue+1 not in visited:
                visited.append(popvalue+1)
                queue.append((popvalue+1,second+1))
            if popvalue-1 not in visited:
                visited.append(popvalue-1)
                queue.append((popvalue-1,second+1))
            if popvalue*2 not in visited:
                visited.append(popvalue*2)
                queue.append((popvalue*2,second+1))

            print(queue)
        