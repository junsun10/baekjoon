# 주사위 굴리기

import sys
from tempfile import tempdir
input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arr_k = list(map(int,input().split()))
dice = [0 for _ in range(7)]
top = 1
bottom = 6
left = 4
right = 3
back = 2
front = 5
# print(arr)
# print(arr_k)


def turn(i):
    global x,y,arr,dice,top,bottom,left,right,back,front
    if i == 1: # 동
        if y+1 >= m:
            return False
        else:
            y += 1
        temp = top
        top = left
        left = bottom
        bottom = right
        right = temp

        

    elif i == 2: # 서
        if y-1 < 0:
            return False
        else:
            y -= 1
        temp = top
        top = right
        right = bottom
        bottom = left
        left = temp

       

    elif i == 3: # 북
        if x-1 < 0:
            return False
        else:
            x -= 1
        temp = top
        top = front
        front = bottom
        bottom = back
        back = temp


    else: # i == 4 # 남
        if x+1 >= n:
            return False
        else:
            x += 1
        temp = top
        top = back
        back = bottom
        bottom = front
        front = temp    


for i in range(k):
    temp = turn(arr_k[i])

    # 배열 벗어나면 넘김
    if temp == False:
        continue

    if arr[x][y] == 0:
        arr[x][y] = dice[bottom]
    else:
        dice[bottom] = arr[x][y]
        arr[x][y] = 0
    print(dice[top])
    # for i in range(n):
    #     print(arr[i])