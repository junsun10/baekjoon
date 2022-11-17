# 입국심사

import sys

n,m = map(int,sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

arr.sort()

max_arr = arr[-1]
min_arr = arr[0]
max_arr_person = 0
for i in arr:
    max_arr_person += max_arr//i
# print(max_arr_person)

time = (m//max_arr_person)*max_arr
print(time)

while True:
    temp = 0
    for i in arr:
        temp += time//i
    # print(temp)
    if temp < m:
        print(time)
        break
    else:
        time -= max_arr
    # print(time)

time = (time//min_arr+1)*min_arr
print(time)

while True:
    temp = 0
    for i in arr:
        temp += time//i
    # print(temp)
    if temp >= m:
        print(time)
        break
    else:
        time += min_arr


# while True:
#     temp = 0
#     for i in arr:
#         temp += time//i
#     # print(temp)
#     if temp < m:
#         print(time+1)
#         break
#     else:
#         time -= 1
#     # print(time)
