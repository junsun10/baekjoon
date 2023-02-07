# 큐 2 ( 정답 )
# 알고리즘 : 큐


import sys
from collections import deque
queue = deque()
for _ in range(int(input())):
    ins = str(sys.stdin.readline())
    if ins[:3] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif ins[:4] == "size":
        print(len(queue))
    elif ins[:4] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif ins[:4] == "push":
        temp = int(ins[5:-1])
        queue.append(temp)
    elif ins[:5] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
