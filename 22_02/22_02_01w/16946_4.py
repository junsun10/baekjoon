# 벽 부수고 이동하기 4 ( 정답 )
# 0이 연결된 애들끼리 그룹을 만들어서 각 그룹에 몇개의 0 이 있는지
# 따로 저장해 놓은 다음 1인 블록 주변을 그룹이 중복되지 않게 센다음
# 따로 저장 된 0의 개수를 더함

import sys
from collections import deque

# N,M 입력
n,m = map(int,sys.stdin.readline().split())

# 맵 입력
arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

# 상 하 좌 우
index_x=[-1,1,0,0]
index_y=[0,0,-1,1]

# def bfs(x,y):

#     queue = deque()
#     queue.append((x,y))
#     visited[x][y] = True
    
#     temp=[]


#     while queue:
#         v,w = queue.popleft()
        
#         for i in range(4):
#             if v+index_x[i] < 0 or w+index_y[i] < 0:
#                 continue
#             elif v+index_x[i] >= n or w+index_y[i] >= m:
#                 continue
#             else:
#                 if visited[v+index_x[i]][w+index_y[i]] == True:
#                     continue

#                 elif arr[v+index_x[i]][w+index_y[i]] == 0:

#                     visited[v+index_x[i]][w+index_y[i]] = True
#                     queue.append((v+index_x[i],w+index_y[i]))
#                     if (arr2[v+index_x[i]][w+index_y[i]]) not in temp:
#                         temp.append(arr2[v+index_x[i]][w+index_y[i]])
#                 else:
#                     continue

#     print(temp)
#     for i in range(len(temp)):
#         arr[x][y] = (arr[x][y] + numarr[temp[i]]) % 10



def bfs(x,y):

    temp=[] # 연합 중복추가 방지
    
    for i in range(4):
        if x+index_x[i] < 0 or y+index_y[i] < 0:
            continue
        elif x+index_x[i] >= n or y+index_y[i] >= m:
            continue
        else:
            if arr[x+index_x[i]][y+index_y[i]] == 0:
                if (arr2[x+index_x[i]][y+index_y[i]]) not in temp:
                    temp.append(arr2[x+index_x[i]][y+index_y[i]])
            else:
                continue

    # print(temp)
    for i in range(len(temp)):
        arr[x][y] = (arr[x][y] + numarr[temp[i]]) % 10


# 연결돼있는 0 끼리 연합 만들기
def bfs2(x,y):

    queue = deque() # bfs위한 큐
    queue.append((x,y))
    visited[x][y] = True # 방문노드

    temp = []   # 연합을 위한 배열
    temp.append((x,y))
    count=1 # 연합에 있는 노드 수 카운트

    while queue:
        v,w = queue.popleft()
        # 상하좌우 방문
        for i in range(4):
            if v+index_x[i] < 0 or w+index_y[i] < 0:
                continue
            elif v+index_x[i] >= n or w+index_y[i] >= m:
                continue
            else:
                if visited[v+index_x[i]][w+index_y[i]] == True:
                    continue

                elif arr[v+index_x[i]][w+index_y[i]] == 0:

                    visited[v+index_x[i]][w+index_y[i]] = True
                    queue.append((v+index_x[i],w+index_y[i]))
                    temp.append((v+index_x[i],w+index_y[i]))
                    count+=1
                else:
                    continue

    
    for x,y in temp:
        arr2[x][y] = number
    numarr.append(count)


visited = [[False for _ in range(m)] for _ in range(n)]
arr2 = [[0 for _ in range(m)] for _ in range(n)] # 연합 표기된 새로운 배열
numarr = [0] # 각 연합의 노드수 저장
number=1 # 몇번째 연합
for i in range(n):
    for j in range(m):
        if arr[i][j]==0 and not visited[i][j]:
            bfs2(i,j)
            number += 1


# visited = [[False for _ in range(m)] for _ in range(n)]


for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            bfs(i,j)



# print()
# for i in range(n):
#     line=""
#     for j in range(m):
#         line+=str(arr2[i][j])
#     print(line)

# print(numarr)

for i in range(n):
    line=""
    for j in range(m):
        line+=str(arr[i][j])
    print(line)