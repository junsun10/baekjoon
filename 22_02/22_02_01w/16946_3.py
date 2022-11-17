# 벽 부수고 이동하기 4 ( 시간 초과 )
# 인접한 통로끼리 그룹 만들기


import sys
from collections import deque

# N,M 입력
n,m = map(int,sys.stdin.readline().split())

# 맵 입력
arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
# print(arr)

# visited = [[False for _ in range(m)] for _ in range(n)]


graph = []

# 상 하 좌 우
index_x=[-1,1,0,0]
index_y=[0,0,-1,1]

def bfs(x,y):

    # visited = [[False for _ in range(m)] for _ in range(n)]
    visited=[]


    queue = deque([[x,y]])
    # print()
    # print("bfs start:",queue)
    visited.append([x,y])
    count=1

    while queue:
        v,w = queue.popleft()
        # print("v,w : ",v,w)
        
        for i in range(4):
            if v+index_x[i] < 0 or w+index_y[i] < 0:
                # print("if:",i)
                continue
            elif v+index_x[i] >= n or w+index_y[i] >= m:
                # print("elif:",i)
                # print(v+index_x[i],w+index_y[i])
                # print()
                continue
            else:
                # print("else:",i)
                if arr[v+index_x[i]][w+index_y[i]] == 0 \
                    and [v+index_x[i],w+index_y[i]] not in visited:

                    # print("else,if:",i)
                    visited.append([v+index_x[i],w+index_y[i]])
                    queue.append([v+index_x[i],w+index_y[i]])
                    # print(queue)
                    count+=1
                else:
                    continue

        # print("queue:",queue)
    # print("count:",count)
    arr[x][y]=count


visited_union=[]

def bfs_union(x,y):

    queue = deque([[x,y]])
    visited_union.append([x,y])

for i in range(n):
    for j in range(m):
        if arr[i][j]==0 and [i,j] not in visited_union:
            bfs_union(i,j)

        
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            bfs(i,j)

for i in range(n):
    line=""
    for j in range(m):
        line+=str(arr[i][j])
    print(line)