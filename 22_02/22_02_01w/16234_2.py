# 인구 이동 ( 정답 )

import sys
from collections import deque

# N,L,R 입력
n, l, r = map(int,sys.stdin.readline().split())

# N*N 배열 입력
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# 상 하 좌 우
index_x=[-1,1,0,0]
index_y=[0,0,-1,1]

# 인구이동 유무
is_move = False


def bfs(x,y):
    global is_move
    count=1 # 연합 국가 수
    temp = [] # 연합
    temp.append((x,y))    
    people = arr[x][y] # 연합 인구
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        v,w = queue.popleft()
        # print("v,w : ",v,w)
        
        # 상하좌우 검색
        for i in range(4):
            
            if v+index_x[i] < 0 or w+index_y[i] < 0:
                # print("if:",i)
                continue
            elif v+index_x[i] >= n or w+index_y[i] >= n:
                # print("elif:",i)
                # print(v+index_x[i],w+index_y[i])
                # print()
                continue

            else:
                # print("else:",i)

                # 방문했을경우
                if visited[v+index_x[i]][w+index_y[i]] == True:
                    continue

                elif ( abs(arr[v][w] - arr[v+index_x[i]][w+index_y[i]]) >= l \
                    and abs(arr[v][w] - arr[v+index_x[i]][w+index_y[i]]) <= r ):

                    # print("else,if:",i)
                    visited[v+index_x[i]][w+index_y[i]] = True
                    # print(visited)
                    queue.append((v+index_x[i],w+index_y[i]))
                    # print(queue)

                    people += arr[v+index_x[i]][w+index_y[i]]
                    count+=1
                    temp.append((v+index_x[i],w+index_y[i]))
                else:
                    continue
    

    if count > 1:
        is_move = True
        for x,y in temp:
            arr[x][y] = people//count # 인구 이동
        # print(arr)



answer = 0

while True:
    is_move = False
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i,j)

    if is_move:
        answer += 1
    else:
        break

print(answer)
