# 뱀과 사다리 게임( 알고리즘 확인 )
# 알고리즘 : bfs
# bfs 사용, 사다리, 뱀 위치시 이동

from collections import deque

n, m = map(int, input().split())
visited = [False for _ in range(101)]
ladder_from = []
ladder_to = []
snake_from = []
snake_to = []
temp = []
for _ in range(n):
    x, y = map(int, input().split())
    temp.append([x, y])
temp.sort()
for x, y in temp:
    ladder_from.append(x)
    ladder_to.append(y)
temp = []
for _ in range(m):
    x, y = map(int, input().split())
    temp.append([x, y])
temp.sort()
for x, y in temp:
    snake_from.append(x)
    snake_to.append(y)

answer = 0
end = False
dq = deque()
dq.append([1, 0])
visited[1] = True
while True:
    x, t = dq.popleft()
    for i in range(1, 7):
        if x+i > 0 and x+i <= 100:
            if x+i == 100:
                answer = t + 1
                end = True
                break
            elif i+x in ladder_from and not visited[i+x]:
                dq.append([ladder_to[ladder_from.index(i+x)], t+1])
                visited[i+x] = True

            elif i+x in snake_from and not visited[i+x]:
                dq.append([snake_to[snake_from.index(i+x)], t+1])
                visited[i+x] = True
            else:
                if not visited[i+x]:
                    dq.append([i+x, t+1])
                    visited[i+x] = True
    if end:
        break
print(answer)
