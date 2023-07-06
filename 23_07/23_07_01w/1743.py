# 음식물 피하기 ( 정답 )
# 알고리즘 : bfs
# 전체 좌표중 음식물이 떨어진 좌표에서 bfs

from collections import deque

n, m, k = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

visited = [[False for _ in range(m)] for _ in range(n)]
max_val = -1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            size = 1
            dq = deque()
            dq.append((i, j))
            visited[i][j] = True

            while dq:
                x, y = dq.popleft()

                for h in range(4):
                    nx, ny = x+dx[h], y+dy[h]
                    if nx >= 0 and nx < n and ny >= 0 and ny < m and arr[nx][ny] == 1 and not visited[nx][ny]:
                        dq.append((nx, ny))
                        visited[nx][ny] = True
                        size += 1
            max_val = max(size, max_val)

print(max_val)
