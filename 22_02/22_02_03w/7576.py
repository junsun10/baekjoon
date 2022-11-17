# 토마토 ( 정답 )

import sys
from collections import deque

# M,N 입력
m,n = map(int,sys.stdin.readline().split())

# arr 입력
arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

# 상 하 좌 우
ind_x = [1, -1, 0, 0]
ind_y = [0, 0, -1, 1]


queue = deque()
count_1 = 0
count_m1 = 0

lenqueue = 0
day = 1
d1 = False

# 1들 큐에 넣음
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append((i,j))
            count_1 += 1
        elif arr[i][j] == -1:
            count_m1 += 1

lenqueue = len(queue)

# 0 없으면 바로 끝
if count_1 + count_m1 == m*n:
    print(0)
    d1 = True


while queue:
    # print("day:",day)
    # print("lenque:",lenqueue)
    # print(queue)

    # day 계산
    if lenqueue == 0:
        day+=1
        lenqueue = len(queue) - 1
    else:
        lenqueue -= 1
    x,y = queue.popleft()


    for i in range(4):
        xm = x + ind_x[i]
        ym = y + ind_y[i]
        if xm < 0 or xm >= n or ym < 0 or ym >= m:
            continue
        elif arr[xm][ym] == 0:
            arr[xm][ym] = 1
            queue.append((xm,ym))
            count_1 += 1
        else:
            continue

    
    # for i in range(n):
    #     print(arr[i])
    # print("day:",day)
    # print("lenque:",lenqueue)
    # print(queue)
    # print()

# 다 못 익은 경우
if count_1 + count_m1 != m*n:
    print(-1)
# 다 익은 경우
if count_1 + count_m1 == m*n and d1 == False:
    print(day-1)


    
