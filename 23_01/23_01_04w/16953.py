# A -> B ( 정답 )
# 알고리즘 : bfs
# 두 배 하는 경우와 10 곱하고 1 더하는 경우 bfs

from collections import deque
a, b = map(int, input().split())

queue = deque()
queue.append((a, 1))
end = False

while len(queue) > 0:
    n, c = queue.popleft()

    temp = n*2
    if temp == b:
        print(c+1)
        end = True
        break
    elif temp > b:
        continue
    else:
        queue.append((temp, c+1))

    temp = n*10 + 1
    if temp == b:
        print(c+1)
        end = True
        break
    elif temp > b:
        continue
    else:
        queue.append((temp, c+1))

if not end:
    print(-1)
