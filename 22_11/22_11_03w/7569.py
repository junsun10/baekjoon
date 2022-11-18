# 토마토 ( 정답 )
# 알고리즘 : BFS
# bfs에 날짜값 추가

from collections import deque

m, n, h = map(int, input().split())
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
answer = 0

dq = deque()
wall = 0
tomato = 0

arr = []
for i in range(h):
    temp = []
    for j in range(n):
        line = list(map(int, input().split()))
        temp.append(line)
        for k in range(m):
            if line[k] == 1:
                dq.append((i, j, k, 0))
                visited[i][j][k] = True
                tomato += 1
            elif line[k] == -1:
                wall += 1
            else:
                continue
    arr.append(temp)

# 위 아래 왼쪽 오른쪽 앞 뒤
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]


while dq:
    z, x, y, t = dq.popleft()

    for i in range(6):
        nz, nx, ny = z+dz[i], x+dx[i], y+dy[i],
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and arr[nz][nx][ny] == 0 and not visited[nz][nx][ny]:
            dq.append((nz, nx, ny, t+1))
            visited[nz][nx][ny] = True
            tomato += 1
            answer = t+1

if tomato+wall == m*n*h:
    print(answer)
else:
    print(-1)
