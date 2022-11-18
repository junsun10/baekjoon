# 적록색약

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
arr = [list(input()) for _ in range(n)]


visited = [[False for _ in range(n)] for _ in range(n)]
count1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dq = deque()
            dq.append((i, j, arr[i][j]))
            visited[i][j] = True
            count1 += 1

            while dq:
                x, y, z = dq.popleft()

                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == z:
                        dq.append((nx, ny, arr[nx][ny]))
                        visited[nx][ny] = True

visited = [[False for _ in range(n)] for _ in range(n)]
count2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dq = deque()
            dq.append((i, j, arr[i][j]))
            visited[i][j] = True
            count2 += 1

            while dq:
                x, y, z = dq.popleft()

                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and (arr[nx][ny] == z or (z == "R" and arr[nx][ny] == "G") or (z == "G" and arr[nx][ny] == "R")):
                        dq.append((nx, ny, arr[nx][ny]))
                        visited[nx][ny] = True

print(count1, count2)
