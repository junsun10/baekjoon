# 전깃줄 ( 시간초과 )

from collections import deque

n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append([b, a])
arr.sort()
answer = -1


def check(index, list):
    global answer
    if index < n:
        if len(list) + (n-index) < answer:
            return

        if (len(list) > 0 and list[-1] < arr[index][1]) or len(list) == 0:
            check(index+1, list+[arr[index][1]])
        check(index+1, list)

    else:
        answer = max(answer, len(list))


check(0, [])
print(n-answer)
