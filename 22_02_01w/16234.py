# 인구 이동 ( 시간 초과 )

import copy
import sys

# N,L,R 입력
n, l, r = map(int,sys.stdin.readline().split())
# print("n:",n," l:",l," r:",r)

# N*N 배열 입력
arr=[]
for i in range(n):
    temp=list(map(int,sys.stdin.readline().split()))
    arr.append(temp)
# print(arr)

############################################################
# # 인접리스트
# nlist = [[0 for _ in range(n*n)] for _ in range(n*n)]

# for i in range(n):
#     for j in range(n):
#         if i==n-1 and j==n-1:
#             continue
#         elif i==n-1:
#             if abs(arr[i][j] - arr[i][j+1]) >= l \
#                 and abs(arr[i][j] - arr[i][j+1]) <= r:
#                 nlist[i*n+j][i*n+(j+1)] = 1
#                 nlist[i*n+(j+1)][i*n+j] = 1
#         elif j==n-1:
#             if abs(arr[i][j] - arr[i+1][j]) >= l \
#                 and abs(arr[i][j] - arr[i+1][j]) <= r:
#                 nlist[i*n+j][(i+1)*n+j] = 1
#                 nlist[(i+1)*n+j][i*n+j] = 1
#         else:
#             if abs(arr[i][j] - arr[i][j+1]) >= l \
#                 and abs(arr[i][j] - arr[i][j+1]) <= r:
#                 nlist[i*n+j][i*n+(j+1)] = 1
#                 nlist[i*n+(j+1)][i*n+j] = 1
#             if abs(arr[i][j] - arr[i+1][j]) >= l \
#                 and abs(arr[i][j] - arr[i+1][j]) <= r:
#                 nlist[i*n+j][(i+1)*n+j] = 1
#                 nlist[(i+1)*n+j][i*n+j] = 1

# for i in range(n*n):
#     for j in range(n*n):
#         if j==n*n-1:
#             print(nlist[i][j])
#         else:
#             print(nlist[i][j],end=" ")

# print()

# # 방문
# visit=[[0 for _ in range(n*n)] for _ in range(n*n)]

# def dfs(x,v):
#     visit[x][v]=1
#     for i in range(n*n):
#         if(visit[x][i]==0 and nlist[v][i]):
#             dfs(x,i)

# for i in range(n*n):
#     dfs(i,i)

# for i in range(n*n):
#     for j in range(n*n):
#         if j==n*n-1:
#             print(visit[i][j])
#         else:
#             print(visit[i][j],end=" ")


# # 연합
# union=[]

# for i in range(n*n):
#     temp=[]
#     for j in range(n*n):
#         if visit[i]==visit[j]:
#             temp.append(j)
#     if temp not in union:
#         union.append(temp)
#     else:
#         continue

# print(union)

# # 이동
# for i in range(len(union)):
#     sum=0
#     for j in range(len(union[i])):
#         temp = union[i][j]
#         sum += arr[temp//n][temp%n]
#     # print(sum//len(union[i]))

#     for j in range(len(union[i])):
#         temp = union[i][j]
#         arr[temp//n][temp%n] = sum//len(union[i])



# for i in range(n):
#     for j in range(n):
#         if j==n-1:
#             print(arr[i][j])
#         else:
#             print(arr[i][j],end=" ")
###################################################

###################################################
count=0

while(True):
    # 인접리스트
    nlist = [[0 for _ in range(n*n)] for _ in range(n*n)]

    for i in range(n):
        for j in range(n):
            if i==n-1 and j==n-1:
                continue
            elif i==n-1:
                if abs(arr[i][j] - arr[i][j+1]) >= l \
                    and abs(arr[i][j] - arr[i][j+1]) <= r:
                    nlist[i*n+j][i*n+(j+1)] = 1
                    nlist[i*n+(j+1)][i*n+j] = 1
            elif j==n-1:
                if abs(arr[i][j] - arr[i+1][j]) >= l \
                    and abs(arr[i][j] - arr[i+1][j]) <= r:
                    nlist[i*n+j][(i+1)*n+j] = 1
                    nlist[(i+1)*n+j][i*n+j] = 1
            else:
                if abs(arr[i][j] - arr[i][j+1]) >= l \
                    and abs(arr[i][j] - arr[i][j+1]) <= r:
                    nlist[i*n+j][i*n+(j+1)] = 1
                    nlist[i*n+(j+1)][i*n+j] = 1
                if abs(arr[i][j] - arr[i+1][j]) >= l \
                    and abs(arr[i][j] - arr[i+1][j]) <= r:
                    nlist[i*n+j][(i+1)*n+j] = 1
                    nlist[(i+1)*n+j][i*n+j] = 1

    for i in range(n*n):
        for j in range(n*n):
            if j==n*n-1:
                print(nlist[i][j])
            else:
                print(nlist[i][j],end=" ")

    print()

    # 방문
    visit=[[0 for _ in range(n*n)] for _ in range(n*n)]

    def dfs(x,v):
        visit[x][v]=1
        for i in range(n*n):
            if(visit[x][i]==0 and nlist[v][i]):
                dfs(x,i)

    for i in range(n*n):
        dfs(i,i)

    for i in range(n*n):
        for j in range(n*n):
            if j==n*n-1:
                print(visit[i][j])
            else:
                print(visit[i][j],end=" ")


    # 연합
    union=[]

    for i in range(n*n):
        temp=[]
        for j in range(n*n):
            if visit[i]==visit[j]:
                temp.append(j)
        if temp not in union:
            union.append(temp)
        else:
            continue

    print(union)

    # break 조건
    if len(union)==n*n:
        print(count)
        break
    count+=1

    # 이동
    for i in range(len(union)):
        sum=0
        for j in range(len(union[i])):
            temp = union[i][j]
            sum += arr[temp//n][temp%n]
        # print(sum//len(union[i]))

        for j in range(len(union[i])):
            temp = union[i][j]
            arr[temp//n][temp%n] = sum//len(union[i])



    for i in range(n):
        for j in range(n):
            if j==n-1:
                print(arr[i][j])
            else:
                print(arr[i][j],end=" ")

################################################


# # 제출용
# count=0

# while(True):
#     # 인접리스트
#     nlist = [[0 for _ in range(n*n)] for _ in range(n*n)]

#     for i in range(n):
#         for j in range(n):
#             if i==n-1 and j==n-1:
#                 continue
#             elif i==n-1:
#                 if abs(arr[i][j] - arr[i][j+1]) >= l \
#                     and abs(arr[i][j] - arr[i][j+1]) <= r:
#                     nlist[i*n+j][i*n+(j+1)] = 1
#                     nlist[i*n+(j+1)][i*n+j] = 1
#             elif j==n-1:
#                 if abs(arr[i][j] - arr[i+1][j]) >= l \
#                     and abs(arr[i][j] - arr[i+1][j]) <= r:
#                     nlist[i*n+j][(i+1)*n+j] = 1
#                     nlist[(i+1)*n+j][i*n+j] = 1
#             else:
#                 if abs(arr[i][j] - arr[i][j+1]) >= l \
#                     and abs(arr[i][j] - arr[i][j+1]) <= r:
#                     nlist[i*n+j][i*n+(j+1)] = 1
#                     nlist[i*n+(j+1)][i*n+j] = 1
#                 if abs(arr[i][j] - arr[i+1][j]) >= l \
#                     and abs(arr[i][j] - arr[i+1][j]) <= r:
#                     nlist[i*n+j][(i+1)*n+j] = 1
#                     nlist[(i+1)*n+j][i*n+j] = 1

#     # 방문
#     visit=[[0 for _ in range(n*n)] for _ in range(n*n)]

#     def dfs(x,v):
#         visit[x][v]=1
#         for i in range(n*n):
#             if(visit[x][i]==0 and nlist[v][i]):
#                 dfs(x,i)

#     for i in range(n*n):
#         dfs(i,i)

#     # 연합
#     union=[]

#     for i in range(n*n):
#         temp=[]
#         for j in range(n*n):
#             if visit[i]==visit[j]: # visit이 같으면 연결돼있으므로 연합
#                 temp.append(j)
#         if temp not in union:
#             union.append(temp)
#         else:
#             continue

#     # break 조건
#     # 연합이 각자이면 중단
#     if len(union)==n*n:
#         print(count)
#         break
#     count+=1

#     # 이동
#     for i in range(len(union)):
#         sum=0
#         # temp값은 0~n*n이므로 노드 위치 환산필요
#         for j in range(len(union[i])):
#             temp = union[i][j]
#             sum += arr[temp//n][temp%n]

#         for j in range(len(union[i])):
#             temp = union[i][j]
#             arr[temp//n][temp%n] = sum//len(union[i])
