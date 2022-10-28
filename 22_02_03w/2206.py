# 벽 부수고 이동하기 ( 시간초과 )

import sys
from collections import deque

# N,M 입력
n,m = map(int,sys.stdin.readline().split())

# arr 입력
arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().strip())))

# 우 하 좌 상
ind_x = [0, -1, 0, 1]
ind_y = [1, 0, -1, 0]

q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i,j))

minlen=[]

while q:
    i,j = q.popleft()
    arr[i][j] = 0
    count = 0
    visited = []
    queue = deque()
    queue.append((0,0,1))
    while queue:
        x,y,c = queue.popleft()
        for k in range(4):
            xm = x + ind_x[k]
            ym = y + ind_y[k]
            if xm < 0 or xm >= n or ym < 0 or ym >= m or (xm,ym) in visited:
                continue
            elif xm == n-1 and ym == m-1:
                minlen.append(c+1)
                break
            elif arr[xm][ym] == 0:
                queue.append((xm,ym,c+1))
                visited.append((xm,ym))
            else:
                continue
    
    arr[i][j] = 1

if len(minlen) == 0:
    print(-1)
else:
    print(min(minlen))

    