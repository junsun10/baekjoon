# 카드 정렬하기 ( 시간초과 )


import sys
from collections import deque

# N 입력
n = int(sys.stdin.readline())

# 카드 입력
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))


arr.sort()
queue = deque(arr)
answer = 0
while True:
    temp = 0
    temp = queue[0] + queue[1]
    answer = answer + temp
    queue.popleft()
    queue.popleft()

    for i in range(len(queue)):
        if temp < queue[i]:
            queue.insert(i,temp)
            break
        else:
            continue


    if len(queue)==1:
        answer = answer + temp + queue[0]
        break
    elif len(queue)==0:
        break
    else:
        continue
   
print(answer)