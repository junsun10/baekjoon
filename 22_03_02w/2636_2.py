# 치즈 ( 정답 )

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
new_arr = [[0 for _ in range(m)] for _ in range(n)]

xy = [[-1,0],[1,0],[0,-1],[0,1]]

time = 0
count = []
while True:
    visited = [[False for _ in range(m)] for _ in range(n)]

    queue = deque()
    queue.append((0,0))
    visited[0][0] = True

    time += 1
    temp = 0

    # 값이 0 인 자리 너비우선탐색
    while queue:
        x,y = queue.popleft()
        # 상하좌우 탐색
        for i in range(4):
            new_x = x+xy[i][0]
            new_y = y+xy[i][1]
            # 판 벗어나지 않을경우
            if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
                if not visited[new_x][new_y]:
                    # 0이면 큐에 더함
                    if arr[new_x][new_y]==0:
                        visited[new_x][new_y] = True
                        queue.append((new_x,new_y))
                    # 1이면 값 0으로 바꾸고 temp 증가
                    elif arr[new_x][new_y]==1:
                        visited[new_x][new_y] = True
                        new_arr[new_x][new_y] = time
                        arr[new_x][new_y] = 0
                        temp+=1

    count.append(temp)

    # print(time)
    # for i in range(n):
    #     print(arr[i])
    # print()
    # for i in range(n):
    #     print(new_arr[i])
    
    if temp == 0:
        print(time-1)
        print(count[time-2])
        break
