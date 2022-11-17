# 치즈 ( 제출 x )

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
new_arr = [[0 for _ in range(m)] for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         new_arr[i][j] = arr[i][j]

# arr[0] = [2 for _ in range(y)]
# arr[-1] = [2 for _ in range(y)]
# for i in range(1,x-1,1):
#     arr[i][0] = 2
#     arr[i][-1] = 2

xy = [[-1,0],[1,0],[0,-1],[0,1]]

# day = 0
# while True:
#     day += 1
# print(day)
visited = [[False for _ in range(m)] for _ in range(n)]

queue = deque()
queue.append((0,0))
visited[0][0] = True
new_arr[0][0] = 2
# temp = []
while queue:
    x,y = queue.popleft()
    for i in range(4):
        new_x = x+xy[i][0]
        new_y = y+xy[i][1]
        if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
            if not visited[new_x][new_y] and arr[new_x][new_y]==0:
                new_arr[new_x][new_y] = 2
                visited[new_x][new_y] = True
                queue.append((new_x,new_y))
            elif not visited[new_x][new_y] and arr[new_x][new_y]==1:
                new_arr[new_x][new_y] = 2
                # visited[new_x][new_y] = True
                # temp.append((new_x,new_y))



# for i in range(1,n-1,1):
#     for j in range(1,m-1,1):
#         for k in range(4):
#             if arr[i+xy[k][0]][j+xy[k][1]] == 0 and arr[i][j]==1:
#                 new_arr[i][j] = 1

for i in range(n):
    print(arr[i])
print()
for i in range(n):
    print(new_arr[i])


# for i in range(1,n-1,1):
#     for j in range(1,m-1,1):
#         for k in range(4):
#             if new_arr[i+xy[k][0]][j+xy[k][1]] == 2 and arr[i][j] == 1:
#                 new_arr[i][j] = 2
#             elif new_arr[i+xy[k][0]][j+xy[k][1]] == 2 and new_arr[i][j] == 0:
#                 new_arr[i][j] = 2

# visited = [[False for _ in range(m)] for _ in range(n)]
# queue = deque()
# queue.append((0,0))
# visited[0][0] = True
# new_arr[0][0] = 2
# while queue:
#     x,y = queue.popleft()
#     for i in range(4):
#         new_x = x+xy[i][0]
#         new_y = y+xy[i][1]
#         if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
#             if not visited[new_x][new_y] and arr[new_x][new_y]==2 and arr[x][y]==1:
#                 new_arr[x][y] = 2
#                 visited[new_x][new_y] = True
#                 queue.append((new_x,new_y))
#             elif not visited[new_x][new_y] and arr[new_x][new_y]==2 and arr[x][y]==0:
#                 new_arr[x][y] = 2
#                 visited[new_x][new_y] = True
#                 queue.append((new_x,new_y))

# print()
# for i in range(n):
#     print(new_arr[i])

# if day == 3:
#     break