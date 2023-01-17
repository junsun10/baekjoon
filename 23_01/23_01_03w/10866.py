# 덱 ( 정답 )
# 알고리즘 : 자료구조

from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
    s = sys.stdin.readline().rstrip()
    if s[:10] == "push_front":
        queue.appendleft(int(s[11:]))
    elif s[:9] == "push_back":
        queue.append(int(s[10:]))
    elif s == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif s == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif s == "size":
        print(len(queue))
    elif s == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif s == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif s == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
