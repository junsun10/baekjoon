# 로봇 청소기


import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
start_x,start_y,start_z = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
# print(arr)
# 북 동 남 서
xy = [[-1,0],[0,1],[1,0],[0,-1]]

x = start_x
y = start_y
z = start_z
count = 0
end = False

while True:
    if arr[x][y] == 0:
        arr[x][y] = 2
        count += 1
        
    # 방향기준 왼쪽 == 3더하고 4로나눈나머지
    # x+xy[(z+3)%4][0], y+xy[(z+3)%4][1]
    temp = 0
    while True:
        # 왼쪽 청소 가능
        if arr[x+xy[(z+3)%4][0]][y+xy[(z+3)%4][1]] == 0:
            # 회전후 이동
            z = (z+3)%4
            x = x+xy[z][0]
            y = y+xy[z][1]
            break
        # 왼쪽 청소 불가능
        elif arr[x+xy[(z+3)%4][0]][y+xy[(z+3)%4][1]] != 0:
            # 회전
            z = (z+3)%4
            temp += 1
        # 네방향 청소 불가능
        if temp == 4:
            # 뒤가 벽이 아닌 청소한 곳이면 뒤로이동
            if arr[x+xy[(z+2)%4][0]][y+xy[(z+2)%4][1]] == 2:
                x = x+xy[(z+2)%4][0]
                y = y+xy[(z+2)%4][1]
                temp = 0
            # 뒤가 벽인경우 종료
            else:
                end = True
                break
    if end:
        break
            
print(count)
            