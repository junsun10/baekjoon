# 쿼드트리

import sys
input = sys.stdin.readline
limit_number = 10000
sys.setrecursionlimit(limit_number)

n = int(input())
in_arr = [list(map(int,input().strip())) for _ in range(n)]
new_arr = []

div = n//2

def first(div,arr):

    temp = []
    for i in range(div):
        for j in range(div):
            temp.append(arr[i][j])
    new_arr.append(temp)

    temp = []
    for i in range(div):
        for j in range(div,n,1):
            temp.append(arr[i][j])
    new_arr.append(temp)

    temp = []
    for i in range(div,n,1):
        for j in range(div):
            temp.append(arr[i][j])
    new_arr.append(temp)

    temp = []
    for i in range(div,n,1):
        for j in range(div,n,1):
            temp.append(arr[i][j])
    new_arr.append(temp)

def divide(div,arr):
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    l = div//2 
    temp1 = arr[0:l] + arr[l*2:l*3]
    temp2 = arr[l:l*2] + arr[l*3:l*4]
    temp3 = arr[l*4:l*5] + arr[l*6:l*7]
    temp4 = arr[l*5:l*6] + arr[l*7:]
    temp1 = decision(temp1)
    temp2 = decision(temp2)
    temp3 = decision(temp3)
    temp4 = decision(temp4)
    if len(temp1) > 4:
        temp1 = divide(div//2,temp1)
    if len(temp2) > 4:
        temp2 = divide(div//2,temp2)
    if len(temp3) > 4:
        temp3 = divide(div//2,temp3)
    if len(temp4) > 4:
        temp4 = divide(div//2,temp4)
    add = []
    add.append(temp1)
    add.append(temp2)
    add.append(temp3)
    add.append(temp4)
    return add

def decision(arr):
    if 0 in arr and 1 not in arr:
        return [0]
    elif 1 in arr and 0 not in arr:
        return [1]
    else:
        return arr

for i in range(n):
    print(in_arr[i])

first(div,in_arr)
print("after first")
for i in range(4):
    print(new_arr[i])
print("divide")
for i in range(4):
    new_arr[i] = divide(div,new_arr[i])
    print(new_arr[i])

