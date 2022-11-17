# 벽 부수고 이동하기 ( 틀림 )

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



visited = [[False for _ in range(m)] for _ in range(n)]

queue = deque()
queue.append((0,0))
while queue:
    x,y = queue.popleft()
    arr[x][y] = 2
    visited[x][y] = True
    for k in range(4):
        xm = x + ind_x[k]
        ym = y + ind_y[k]
        if xm < 0 or xm >= n or ym < 0 or ym >= m or visited[xm][ym]:
            continue
        elif arr[xm][ym] == 0:
            queue.append((xm,ym))
            visited[xm][ym] = True
            arr[xm][ym] = 2
        else:
            continue

# for i in range(n):
#     print(arr[i])


if visited[n-1][m-1] == False:
    queue.append((n-1,m-1))
    while queue:
        x,y = queue.popleft()
        arr[x][y] = 3
        visited[x][y] = True
        for k in range(4):
            xm = x + ind_x[k]
            ym = y + ind_y[k]
            if xm < 0 or xm >= n or ym < 0 or ym >= m or visited[xm][ym]:
                continue
            elif arr[xm][ym] == 0:
                queue.append((xm,ym))
                visited[xm][ym] = True
                arr[xm][ym] = 3
            else:
                continue

# for i in range(n):
#     print(arr[i])

wall = []

for i in range(n):
    for j in range(m):
        if (not visited[i][j]) and arr[i][j] == 1:
            wall.append((i,j))

# print(wall)

new_wall = []
for i in wall:
    isnear = []
    for j in range(4):
        xm = i[0] + ind_x[j]
        ym = i[1] + ind_y[j]
        if xm < 0 or xm >= n or ym < 0 or ym >= m:
            continue
        elif arr[xm][ym] == 2:
            isnear.append(2)
        elif arr[xm][ym] == 3:
            isnear.append(3)
    # print(i,isnear)
    if 2 in isnear and 3 in isnear:
        new_wall.append((i))

# print(new_wall)


minlen = []
if len(new_wall) == 0:
    # visited = [[False for _ in range(m)] for _ in range(n)]
    visited =[]
    end = False
    lenqueue = 1
    day = 1
    queue = deque()
    queue.append((0,0))
    # visited[0][0]=True
    visited.append((0,0))
    while queue:

        if lenqueue == 0:
            day+=1
            lenqueue = len(queue) - 1
        else:
            lenqueue -= 1


        x,y = queue.popleft()
        # visited[x][y]=True
        visited.append((x,y))
        for k in range(4):
            xm = x + ind_x[k]
            ym = y + ind_y[k]
            if xm < 0 or xm >= n or ym < 0 or ym >= m:
                continue
            elif xm == n-1 and ym == m-1:
                minlen.append(day+1)
                end = True
                break
            elif (arr[xm][ym] == 2 or arr[xm][ym] == 3)\
                and ((xm,ym) not in visited):

                queue.append((xm,ym))
                # visited[xm][ym]==True
                visited.append((xm,ym))
                # print(queue)
            else:
                continue

        if end:
            break

if len(new_wall)!=0:

    

    for i in new_wall:
        a=i[0]
        b=i[1]
        arr[a][b] = 2

        # for i in range(n):
        #     print(arr[i])


        # 최솟값 구하는 부분
        # visited = [[False for _ in range(m)] for _ in range(n)]
        visited = []
        end = False
        lenqueue = 1
        day = 1
        queue = deque()
        queue.append((0,0))
        # visited[0][0]=True
        visited.append((0,0))
        while queue:

            if lenqueue == 0:
                day+=1
                lenqueue = len(queue) - 1
            else:
                lenqueue -= 1


            x,y = queue.popleft()
            # visited[x][y]=True
            visited.append((x,y))
            for k in range(4):
                xm = x + ind_x[k]
                ym = y + ind_y[k]
                if xm < 0 or xm >= n or ym < 0 or ym >= m:
                    continue
                elif xm == n-1 and ym == m-1:
                    minlen.append(day+1)
                    end = True
                    break
                elif (arr[xm][ym] == 2 or arr[xm][ym] == 3)\
                    and ((xm,ym) not in visited):

                    queue.append((xm,ym))
                    # visited[xm][ym]==True
                    visited.append((xm,ym))
                    # print(queue)
                else:
                    continue

            if end:
                break


        arr[a][b] = 1

        # for i in range(n):
        #     print(arr[i])

# print(minlen)
if len(minlen)==0:
    print(-1)
else:
    print(min(minlen))





