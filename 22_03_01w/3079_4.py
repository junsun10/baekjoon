# 입국심사 ( 정답 )
# 걸리는 시간 계산 이분탐색 사용


import sys

n,m = map(int,sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
# arr.sort()
# max_arr = arr[-1]
max_arr = max(arr)


max_time = max_arr*(m//n)
min_time = 1
time = (max_time+min_time)//2
up_down = ""
while True:
    temp = 0
    for i in arr:
        temp += time//i
    # print()
    # print("time, max min:",time,max_time,min_time)
    # print("temp:",temp)

    if max_time <= min_time:
        if temp < m:
            up_down = "up"
            break
        else:
            up_down = "down"
            break

    # if temp < m:
    #     min_time = time+1
    #     time = (max_time+min_time)//2
    # elif temp > m:
    #     max_time = time-1
    #     time = (max_time+min_time)//2
    # else:
    #     print("==")
    #     break

    # 위 코드를 아래로 바꿨더니 시간초과 해결
    # 같아도 포함
    if temp < m:
        min_time = time+1
        time = (max_time+min_time)//2
    else: # temp >= m:
        max_time = time
        time = (max_time+min_time)//2

# print("time, max, min:",time,max_time,min_time)        
# print(up_down)

if up_down == "up":
    while True:
        temp = 0
        for i in arr:
            temp += time//i
        # print(temp)
        if temp > m:
            print(time)
            break
        else:
            time += 1
        # print(time)

else:
    while True:
        temp = 0
        for i in arr:
            temp += time//i
        # print(temp)
        if temp < m:
            print(time+1)
            break
        else:
            time -= 1
        # print(time)