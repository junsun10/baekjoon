# 입국심사

import sys

n,m = map(int,sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

arr.sort()

time = arr[n//2]*(m//n)
max_time = arr[-1]*(m//n)
min_time = arr[0]*(m//n)



def search_time(time,x):
    global max_time
    global min_time
    if x=="big":
        max_time = time-1
    else:
        min_time = time

    time = (max_time+min_time)//2
    return time

time = min(arr)
before_time = min(arr)
while True:
    temp = 0
    for i in arr:
        temp += time//i
    print(temp)
    if m == temp:
        print(time-time%arr[0])
        break
    elif m < temp:
        before_time = time
        time = search_time(time,"big")
    else:
        before_time = time
        time = search_time(time,"small")
    print("maxtime, mintime, time",max_time,min_time,time)
    if before_time == time:
        print(time+1)
        break
