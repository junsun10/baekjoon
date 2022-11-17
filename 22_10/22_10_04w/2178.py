# 미로탐색
# 알고리즘 : BFS
# 가능한 방향으로 BFS

from collections import deque

n, m = map(int, input().split())

arr = []
for i in range(n):
    temp = []
    s = input()
    for j in s:
        temp.append(int(j))
    arr.append(temp)
visited = [[False for _ in range(m)]for _ in range(n)]
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque()
dq.append((0, 0, 1))
visited[0][0] = True
end = False

while dq:
    x, y, z = dq.popleft()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m and arr[nx][ny] == 1 and not visited[nx][ny]:
            dq.append((nx, ny, z+1))
            visited[nx][ny] = True
            if nx == n-1 and ny == m-1:
                print(z+1)
                end = True
                break

    if end:
        break
