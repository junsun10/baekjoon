# 계단 오르기 ( 메모리 초과 )

from collections import deque

numOfStairs = int(input())
stairsArr = [int(input()) for _ in range(numOfStairs)]
que = deque()
que.append([0, 1])
que.append([1, 0])
que.append([1, 1])

while True:
    now = que.popleft()

    if len(now) == numOfStairs:
        que.appendleft(now)
        break

    if len(now) == numOfStairs - 1:
        if now[-2] == 0 and now[-1] == 1:
            temp = now[:]
            temp.append(1)
            que.append(temp)
        elif now[-1] == 0:
            temp = now[:]
            temp.append(1)
            que.append(temp)
    else:
        if now[-2] == 0 and now[-1] == 1:
            temp = now[:]
            temp.append(0)
            que.append(temp)
            temp = now[:]
            temp.append(1)
            que.append(temp)
        elif now[-2] == 1 and now[-1] == 1:
            temp = now[:]
            temp.append(0)
            que.append(temp)
        elif now[-1] == 0:
            temp = now[:]
            temp.append(1)
            que.append(temp)

answer = 0
for i in que:
    temp = 0
    if i[-1] == 0:
        continue
    for j in range(len(i)):
        if i[j] == 1:
            temp += stairsArr[j]
    if temp > answer:
        answer = temp

print(answer)
