# 입국심사

import sys

n,m = map(int,sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

# arr.sort()

# max_arr = arr[-1]
# min_arr = arr[0]
# arr_person = [0 for _ in range(n)]

# for i in range(len(arr)-1,-1,-1):
#     for j in range(0,i+1):
#         arr_person[i] += arr[i]//arr[j]
# print(arr_person)

# time = (m//arr_person[-1])*max_arr
# print(time)


answer_arr = [0 for _ in range(n)]
answer = 0
min_arr = min(arr)
time = min_arr

while True:
    for i in range(len(arr)):
        if time%arr[i]==0:
            answer_arr[i] += 1
        # print(answer_arr)

    if sum(answer_arr) >= m:
        print(time)
        break

    time += min_arr

# print(439+439//2+439//3+439//4+439//5)