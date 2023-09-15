# 뮤탈리스크 ( 오답 )

from collections import deque

n = int(input())
arr = list(map(int, input().split()))

dq = deque()
dq.append(arr+[0])
answer = []
min_answer = 61

dp = []
dp_c = []

while dq:
    print(dq)
    temp = dq.popleft()
    scv = temp[:-1]
    count = temp[-1]

    if count >= min_answer:
        continue

    if n == 1:
        if scv[0] <= 0:
            answer.append(count)
            min_answer = min(answer)
        else:
            dq.append([scv[0]-9, count+1])
    elif n == 2:
        if scv[0] <= 0 and scv[1] <= 0:
            answer.append(count)
            min_answer = min(answer)
        else:
            dq.append([scv[0]-9, scv[1]-3, count+1])
            dq.append([scv[0]-3, scv[1]-9, count+1])
    else:
        if scv[0] <= 0 and scv[1] <= 0 and scv[2] <= 0:
            answer.append(count)
            min_answer = min(answer)
        else:
            dq.append([scv[0]-9, scv[1]-3, scv[2]-1, count+1])
            dq.append([scv[0]-9, scv[1]-1, scv[2]-3, count+1])
            dq.append([scv[0]-3, scv[1]-9, scv[2]-1, count+1])
            dq.append([scv[0]-3, scv[1]-1, scv[2]-9, count+1])
            dq.append([scv[0]-1, scv[1]-9, scv[2]-3, count+1])
            dq.append([scv[0]-1, scv[1]-3, scv[2]-9, count+1])


print(min(answer))
