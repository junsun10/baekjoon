# 그림 ( 정답 )
# 알고리즘 : bfs

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False for _ in range(m)] for _ in range(n)]
pictures = []
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue

        if arr[i][j] == 0:
            continue

        dq = deque()
        dq.append((i, j))
        visited[i][j] = True
        size = 1

        while dq:
            x, y = dq.popleft()
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                    dq.append((nx, ny))
                    visited[nx][ny] = True
                    size += 1

        pictures.append(size)

if len(pictures) == 0:
    print(0)
    print(0)
else:
    print(len(pictures))
    print(max(pictures))
