# 영역 구하기 ( 정답 )

import sys
from collections import deque

# M, N, K 입력
m,n,k = map(int,sys.stdin.readline().split())

# arr 입력
arr = []
for _ in range(k):
    arr.append(list(map(int,sys.stdin.readline().split())))

# 상 하 좌 우
ind_x = [1, -1, 0, 0]
ind_y = [0, 0, -1, 1]

# 방문 기록
visited = [[False for _ in range(n)] for _ in range(m)]

# m*n 칸 좌표로 변환
# 직사각형 부분 True로 변경
for i in arr:
    x0 = (m-i[1])-1
    y0 = i[0]
    x1 = (m-i[3])
    y1 = i[2]-1
    for x in range(x1,x0+1):
        for y in range(y0,y1+1):
            if visited[x][y] == False:
                visited[x][y] = True

# 영역
union = []

queue = deque()

# bfs
for i in range(m):
    for j in range(n):

        # 방문했거나 직사각형부분
        if visited[i][j] == True:
            continue
        else:
            queue.append((i,j))
            count = 1
            while queue:
                x,y = queue.popleft()
                visited[x][y] = True
                # 상하좌우 검색
                for k in range(4):
                    xm = x + ind_x[k]
                    ym = y + ind_y[k]
                    if xm < 0 or xm >= m or ym < 0 or ym >= n:
                        continue
                    elif visited[xm][ym] == False:
                        visited[xm][ym] = True
                        queue.append((xm,ym))
                        count+=1
                    else:
                        continue
            # 영역 크기 저장
            union.append(count)
        


print(len(union))
union.sort()
for i in range(len(union)):
    print(union[i],end=" ")
