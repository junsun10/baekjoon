# 감시

import sys
from collections import deque
input = sys.stdin.readline

def south(x,y):
    for i in range(x,n,1):
        if new_arr[i][y] == 0:
            new_arr[i][y] = 7
        elif new_arr[i][y] == 6:
            break
        else:
            continue

def north(x,y):
    for i in range(x,-1,-1):
        if new_arr[i][y] == 0:
            new_arr[i][y] = 7
        elif new_arr[i][y] == 6:
            break
        else:
            continue

def east(x,y):
    for i in range(y,m,1):
        if new_arr[x][i] == 0:
            new_arr[x][i] = 7
        elif new_arr[x][i] == 6:
            break
        else:
            continue

def west(x,y):
    for i in range(y,-1,-1):
        if new_arr[x][i] == 0:
            new_arr[x][i] = 7
        elif new_arr[x][i] == 6:
            break
        else:
            continue

def count_south(x,y,temp):
    for i in range(x,n,1):
        if new_arr[i][y] == 0:
            temp += 1
        elif new_arr[i][y] == 6:
            break
        else:
            continue
    return temp

def count_north(x,y,temp):
    for i in range(x,-1,-1):
        if new_arr[i][y] == 0:
            temp += 1
        elif new_arr[i][y] == 6:
            break
        else:
            continue
    return temp

def count_east(x,y,temp):
    for i in range(y,m,1):
        if new_arr[x][i] == 0:
            temp += 1
        elif new_arr[x][i] == 6:
            break
        else:
            continue
    return temp

def count_west(x,y,temp):
    for i in range(y,-1,-1):
        if new_arr[x][i] == 0:
            temp += 1
        elif new_arr[x][i] == 6:
            break
        else:
            continue
    return temp


n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
new_arr = []
for i in range(n):
    new_arr.append(arr[i][:])

c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
wall = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            c1.append((i,j))
        elif arr[i][j] == 2:
            c2.append((i,j))
        elif arr[i][j] == 3:
            c3.append((i,j))
        elif arr[i][j] == 4:
            c4.append((i,j))
        elif arr[i][j] == 5:
            c5.append((i,j))
        elif arr[i][j] == 6:
            wall.append((i,j))
        else:
            continue

# 5번 cctv
for x,y in c5:
    south(x,y)
    north(x,y)
    east(x,y)
    west(x,y)


# for i in range(n):
#     print(new_arr[i])

# 4번 cctv
for x,y in c4:

    # 최소 카운트
    temp = 0
    count = []
    temp = count_south(x,y,temp)

    count.append(temp)
    temp = 0
    temp = count_north(x,y,temp)

    count.append(temp)
    temp = 0
    temp = count_east(x,y,temp)

    count.append(temp)
    temp = 0
    temp = count_west(x,y,temp)

    count.append(temp)


    # 남쪽이 최소일때
    if min(count) == count[0]:
        north(x,y)
        east(x,y)
        west(x,y)
    
    # 북쪽이 최소일때
    elif min(count) == count[1]:
        south(x,y)
        east(x,y)
        west(x,y)

    # 동쪽이 최소일때
    elif min(count) == count[2]:
        south(x,y)
        north(x,y)
        west(x,y)
    
    # 서쪽이 최소일때
    else:
        south(x,y)
        north(x,y)
        east(x,y)
        

# print()
# for i in range(n):
#     print(new_arr[i])


# 3번 cctv
for x,y in c3:

    # 최소 카운트
    temp = 0
    count = []
    temp = count_south(x,y,temp)

    count.append(temp)
    temp = 0
    temp = count_north(x,y,temp)

    count.append(temp)
    temp = 0
    temp = count_east(x,y,temp)

    count.append(temp)
    temp = 0
    temp = count_west(x,y,temp)

    count.append(temp)
    # print(count)
    # 북,동 / 동,남 / 남,서 / 서,북
    count2 = [count[1]+count[2],count[2]+count[0],count[0]+count[3],count[3]+count[1]]
    # print(count2)

    if max(count2) == count[1]+count[2]:
        north(x,y)
        east(x,y)

    elif max(count2) == count[2]+count[0]:
        south(x,y)
        east(x,y)
    
    elif max(count2) == count[0]+count[3]:
        south(x,y)
        west(x,y)
    
    else:
        north(x,y)
        west(x,y)


# print()
# for i in range(n):
#     print(new_arr[i])

# 2번 cctv
for x,y in c2:

    # 최소 카운트
    temp = 0
    count = []
    temp = count_south(x,y,temp)

    count.append(temp)
    temp = 0
    temp = count_north(x,y,temp)

    count.append(temp)
    temp = 0
    temp = count_east(x,y,temp)

    count.append(temp)
    temp = 0
    temp = count_west(x,y,temp)

    count.append(temp)
    # print(count)
    # 북,남 / 동,서
    count2 = [count[0]+count[1],count[2]+count[3]]
    # print(count2)

    if max(count2) == count[0]+count[1]:
        north(x,y)
        south(x,y)

    else:
        west(x,y)
        east(x,y)

# print()
# for i in range(n):
#     print(new_arr[i])

# 1번 cctv
for x,y in c1:

    # 최소 카운트
    temp = 0
    count = []
    temp = count_south(x,y,temp)

    count.append(temp)
    temp = 0
    temp = count_north(x,y,temp)

    count.append(temp)
    temp = 0
    temp = count_east(x,y,temp)

    count.append(temp)
    temp = 0
    temp = count_west(x,y,temp)

    count.append(temp)

    # print(count)

    # 남쪽이 최대일때
    if max(count) == count[0]:
        south(x,y)
    
    # 북쪽이 최대일때
    elif max(count) == count[1]:
        north(x,y)

    # 동쪽이 최대일때
    elif max(count) == count[2]:
        east(x,y)
    
    # 서쪽이 최대일때
    else:
        west(x,y)

# print()
# for i in range(n):
#     print(new_arr[i])


answer = 0
for i in range(n):
    for j in range(m):
        if new_arr[i][j] == 0:
            answer += 1

print(answer)