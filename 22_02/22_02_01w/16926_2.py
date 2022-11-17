# 배열 돌리기 ( 정답 )

import sys

# N,M,R 입력
n, m, r = map(int,sys.stdin.readline().split())

# N*M 배열 입력
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# print(arr)

def spin(x,y):

    # 테두리 왼쪽 위 값 저장
    before = arr[n-x][m-y]

    # 좌                                           
    for i in range(n-x+1,x):# 1,2,3                #  x x x x
        temp = arr[i][m-y]                         #  o x x x
        arr[i][m-y] = before                       #  o x x x
        before = temp                              #  o x x x
        
    # 하
    for i in range(m-y+1,y):# 1,2,3
        temp = arr[x-1][i]
        arr[x-1][i] = before
        before = temp

    # 우
    for i in range(x-2,n-x-1,-1):# 2,1,0
        temp = arr[i][y-1]
        arr[i][y-1] = before
        before = temp

    # 상
    for i in range(y-2,m-y-1,-1):# 2,1,0
        temp = arr[n-x][i]
        arr[n-x][i] = before
        before = temp

# r번 회전
for i in range(r):
    # 안쪽 테두리로 들어감
    for j in range(min(n,m)//2):
        spin(n-j,m-j)


# 출력
for i in range(n):
    for j in range(m):
        if j==m-1:
            print(arr[i][j])
        else:
            print(arr[i][j],end=" ")