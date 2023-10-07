# 쉬운 최단거리 ( 정답 )
# 알고리즘: bfs
# 목표지점에서 bfs 진행

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer_arr = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            answer_arr[i][j] = 0

goal = []
for i in range(n):
    if 2 in arr[i]:
        goal = [i, arr[i].index(2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False for _ in range(m)] for _ in range(n)]

dq = deque()
dq.append((goal[0], goal[1], 0))
visited[goal[0]][goal[1]] = True
answer_arr[goal[0]][goal[1]] = 0

while dq:
    x, y, c = dq.popleft()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if (0 <= nx < n) and (0 <= ny < m) and arr[nx][ny] == 1 and not visited[nx][ny]:
            dq.append((nx, ny, c+1))
            answer_arr[nx][ny] = c+1
            visited[nx][ny] = True

for i in range(n):
    for j in range(m):
        print(answer_arr[i][j], end=" ")
    print()
