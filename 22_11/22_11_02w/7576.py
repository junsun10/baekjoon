# 토마토 ( 정답 )
# 알고리즘 : BFS
# 익은 토마토를 큐에 넣은 뒤 bfs
# 걸린 시간도 큐에 같이 넣어서 정답 계산

from collections import deque

width, height = map(int, input().split())
boxArr = [list(map(int, input().split())) for _ in range(height)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ripeTomatoes = []
countNotRipeTomatoes = 0
answer = 0

for i in range(height):
    for j in range(width):
        if boxArr[i][j] == 1:
            ripeTomatoes.append((i, j))
        elif boxArr[i][j] == 0:
            countNotRipeTomatoes += 1

dq = deque()
for x, y in ripeTomatoes:
    dq.append((x, y, 0))

while dq:
    x, y, t = dq.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < height and 0 <= ny < width and boxArr[nx][ny] == 0:
            dq.append((nx, ny, t+1))
            boxArr[nx][ny] = 1
            countNotRipeTomatoes -= 1
            answer = t + 1

if countNotRipeTomatoes == 0:
    print(answer)
else:
    print(-1)
