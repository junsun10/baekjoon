# 두 용액 ( 메모리 초과 )
# 두 포인터 사용했지만 재귀가 깊어저 메모리 초과가 된 것으로 보임

import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

def check(i,j):
    global answer, answer_list
    if i == j:
        return
    
    temp = arr[i] + arr[j]

    if abs(temp) < answer:
        answer = temp
        answer_list = [arr[i],arr[j]]

    if temp > 0:
        check(i,j-1)
    elif temp < 0:
        check(i+1,j)
    else:
        return

if arr[-1] <= 0:
    print(arr[-1],arr[-2])
elif arr[0]>= 0:
    print(arr[0],arr[1])
else:
    answer = 2000000000
    answer_list = []
    check(0,n-1)
    print(answer_list)






