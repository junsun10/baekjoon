# 카드2 ( 정답 )
# 알고리즘 : 큐

from collections import deque

n = int(input())
queue = deque()
for i in range(n):
    queue.append(i+1)

if n == 1:
    print(1)
else:
    while True:
        queue.popleft()
        if len(queue) == 1:
            print(queue.pop())
            break
        else:
            temp = queue.popleft()
            queue.append(temp)
