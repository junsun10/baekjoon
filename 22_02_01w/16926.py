# 배열 돌리기 ( 시간 초과 )

import copy

# N,M,R 입력
n, m, r = map(int,input().split())
# print("n:",n," m:",m," r:",r)

# N*M 배열 입력
arr=[]
for i in range(n):
    temp=list(map(int,input().split()))
    arr.append(temp)
# print(arr)

# # 깊은복사
# arr2=copy.deepcopy(arr)

arr2=[[0 for _ in range(m)] for _ in range(n)]

def spin(x,y):
    for i in range(n-x,x):
        if i==n-x:
            for j in range(m-y,y-1):
                arr2[i][j]=arr[i][j+1]
            arr2[i][y-1]=arr[i+1][y-1]
        elif i==(x-1):
            arr2[i][m-y]=arr[i-1][m-y]
            for j in range(m-y+1,y):
                arr2[i][j]=arr[i][j-1]
        else:
            arr2[i][m-y]=arr[i-1][m-y]
            arr2[i][y-1]=arr[i+1][y-1]

for i in range(r):
    for j in range(min(n,m)//2):
        spin(n-j,m-j)
    arr=copy.deepcopy(arr2)

# for i in range(n):
#     print(arr[i])
# print()
# for i in range(n):
#     print(arr2[i])

for i in range(n):
    for j in range(m):
        if j==m-1:
            print(arr2[i][j])
        else:
            print(arr2[i][j],end=" ")

    