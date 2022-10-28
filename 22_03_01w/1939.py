# 중량제한

import sys
from collections import deque


n,m = map(int,sys.stdin.readline().split())
w = [[] for _ in range(n+1)]

def bfs(mid):
    visited[start] = True
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        if now == end:
            return True
        for y, z in w[now]:
            if not visited[y] and z >= mid:
                queue.append(y)
                visited[y] = True
    
    return False

for _ in range(m):
    x,y,z = map(int,sys.stdin.readline().split())
    w[x].append((y,z))
    w[y].append((x,z))

for i in range(n):
    w[i].sort(reverse=True)

start,end = map(int,sys.stdin.readline().split())
low, high = 1, 100000000
while low <= high:
    visited = [ False for _ in range(n+1)]
    mid = (low+high)//2
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1

print(high)

