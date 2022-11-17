# 쿼드트리

import sys
input = sys.stdin.readline

n = int(input())
in_arr = [list(map(int,input().strip())) for _ in range(n)]

def left_top(div,arr):
    if div == 1:
        return

    temp = []
    count0 = 0
    count1 = 0
    for i in range(div):
        for j in range(div):
            if arr[i][j] == 0:
                count0 += 1
            else:
                count1 += 1
            temp.append(arr[i][j])

    if count0 == div*div:
        arr[0] = [0]
    elif count1 == div*div:
        arr[0] = [1]
    else:
        tree(div//2,arr[0])

def right_top(div,arr):
    if div == 1:
        return
        
    temp = []
    count0 = 0
    count1 = 0
    for i in range(div):
        for j in range(div,n,1):
            if arr[i][j] == 0:
                count0 += 1
            else:
                count1 += 1
            temp.append(arr[i][j])

    if count0 == div*div:
        arr[1] = [0]
    elif count1 == div*div:
        arr[1] = [1]
    else:
        tree(div//2,arr[1])

def left_bottom(div,arr):
    if div == 1:
        return
        
    temp = []
    count0 = 0
    count1 = 0
    for i in range(div,n,1):
        for j in range(div):
            if arr[i][j] == 0:
                count0 += 1
            else:
                count1 += 1
            temp.append(arr[i][j])

    if count0 == div*div:
        arr[2] = [0]
    elif count1 == div*div:
        arr[2] = [1]
    else:
        tree(div//2,arr[2])

def right_bottom(div,arr):
    if div == 1:
        return
        
    temp = []
    count0 = 0
    count1 = 0
    for i in range(div,n,1):
        for j in range(div,n,1):
            if arr[i][j] == 0:
                count0 += 1
            else:
                count1 += 1
            temp.append(arr[i][j])

    if count0 == div*div:
        arr[3] = [0]
    elif count1 == div*div:
        arr[3] = [1]
    else:
        tree(div//2,arr[3])

def dfs(div,arr):
    if div == 1:
        return

    temp = []
    count0 = 0
    count1 = 0
    for i in range(div):
        for j in range(div):
            if arr[i][j] == 0:
                count0 += 1
            else:
                count1 += 1
            temp.append(arr[i][j])

    if count0 == div*div:
        print(arr)
        arr = [0]
        print(arr)
    elif count1 == div*div:
        print(arr)
        arr = [1]
        print(arr)
    else:
        dfs(div//2,arr)


def first_tree(div, arr):
    global new_arr
    temp = []
    temp2 = []
    count0 = 0
    count1 = 0
    for i in range(div):
        temp = []
        for j in range(div):
            if arr[i][j] == 0:
                count0 += 1
            else:
                count1 += 1
            temp.append(arr[i][j])
        temp2.append(temp)

    if count0 == div*div:
        new_arr.append([0])
    elif count1 == div*div:
        new_arr.append([1])
    else:
        new_arr.append(temp2)

    temp = []
    temp2 = []
    count0 = 0
    count1 = 0
    for i in range(div):
        temp = []
        for j in range(div,n,1):
            if arr[i][j] == 0:
                count0 += 1
            else:
                count1 += 1
            temp.append(arr[i][j])
        temp2.append(temp)

    if count0 == div*div:
        new_arr.append([0])
    elif count1 == div*div:
        new_arr.append([1])
    else:
        new_arr.append(temp2)

    temp = []
    temp2 = []
    count0 = 0
    count1 = 0
    for i in range(div,n,1):
        temp = []
        for j in range(div):
            if arr[i][j] == 0:
                count0 += 1
            else:
                count1 += 1
            temp.append(arr[i][j])
        temp2.append(temp2)

    if count0 == div*div:
        new_arr.append([0])
    elif count1 == div*div:
        new_arr.append([1])
    else:
        new_arr.append(temp2)

    temp = []
    temp2 = []
    count0 = 0
    count1 = 0
    for i in range(div,n,1):
        temp = []
        for j in range(div,n,1):
            if arr[i][j] == 0:
                count0 += 1
            else:
                count1 += 1
            temp.append(arr[i][j])
        temp2.append(temp)

    if count0 == div*div:
        new_arr.append([0])
    elif count1 == div*div:
        new_arr.append([1])
    else:
        new_arr.append(temp2)

    for i in range(4):
        print(new_arr[i])
    

def tree(div, arr):
    
    # if arr[0] != 1 or arr[0] != 0:
    #     dfs(div,arr[0])
    # if arr[1] != 1 or arr[1] != 0:
    #     dfs(div,arr[1])
    # if arr[2] != 1 or arr[2] != 0:
    #     print(type(arr[2]))
    #     dfs(div,arr[2])
    # if arr[3] != 1 or arr[3] != 0:
    #     dfs(div,arr[3])
    if len(arr[0]) != 1:
        dfs(div,arr[0])
    if len(arr[1]) != 1:
        dfs(div,arr[1])
    if len(arr[2]) != 1:
        print(type(arr[2]))
        dfs(div,arr[2])
    if len(arr[3]) != 1:
        dfs(div,arr[3])




div = int(n/2)
count0 = 0
count1 = 0

new_arr = []

for i in range(n):
    print(in_arr[i])

first_tree(div,in_arr)
div = div//2


dfs(div,new_arr)

print(new_arr)