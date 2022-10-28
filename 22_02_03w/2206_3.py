# 벽 부수고 이동하기 ( 정답 )

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

# visieted[][][0]:벽안부순 경우 visited[][][1]:벽부순경우
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

end=False
queue = deque()
queue.append((0,0,0))
visited[0][0][0] = 1

while queue:
    x,y,c = queue.popleft()
    if x==n-1 and y==m-1:
        print(visited[x][y][c])
        end=True
        break
    for k in range(4):
        xm = x + ind_x[k]
        ym = y + ind_y[k]
        if xm < 0 or xm >= n or ym < 0 or ym >= m:
            continue

        # 벽 안부수는 경우
        if arr[xm][ym]==0 and visited[xm][ym][c]==0:
            queue.append((xm,ym,c))
            visited[xm][ym][c] = visited[x][y][c]+1
        # 벽 부수는 경우
        if arr[xm][ym]==1 and c==0:
            queue.append((xm,ym,c+1))
            visited[xm][ym][c+1] = visited[x][y][c]+1

        # for i in range(n):
        #     print(visited[i])
        # print(queue)
        # print()

if end==False:
    print(-1)