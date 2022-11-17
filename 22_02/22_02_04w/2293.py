# 동전 1 ( 시간초과 )

import sys

n,k = map(int,sys.stdin.readline().split())

arr = list(int(sys.stdin.readline()) for _ in range(n));
arr.sort(reverse=True)
# print(arr)

answer = 0

# def count(k,now):
#     global answer
#     for i in range(k,len(arr)):
#         if now-arr[i] >= 0:
#             # print(arr[i])
#             # print(now-arr[i])
#             if now-arr[i]==0:
#                 answer+=1
#             count(i,now-arr[i]);


def count(k,now):
    global answer
    for i in range(k,len(arr)):
        if now-arr[i] < 0:
            continue
        elif now-arr[i]==0:
            answer+=1
            continue
        else: #now-arr[i] > 0:
            # print(arr[i])
            # print(now-arr[i])
            
            count(i,now-arr[i]);


count(0,k)
print(answer)