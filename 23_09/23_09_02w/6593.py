# 상범 빌딩 ( 정답 )
# 알고리즘: bfs
# 동서남북상하 6가지 경우의 수 bfs 이용해 탐색

from collections import deque

# 동서남북상하
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while True:

    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    arr = []
    start = [0, 0, 0]
    end = [0, 0, 0]
    answer = []

    for i in range(l):
        floor = []
        for j in range(r):
            temp = list(input())
            if 'S' in temp:
                start = [i, j, temp.index('S')]
            if 'E' in temp:
                end = [i, j, temp.index('E')]
            floor.append(temp)
        arr.append(floor)
        temp = input()

    visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(l)]
    dq = deque()
    dq.append((start[0], start[1], start[2], 0))

    while dq:
        z, x, y, t = dq.popleft()

        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]

            if nx >= 0 and nx < r and ny >= 0 and ny < c and nz >= 0 and nz < l:
                if arr[nz][nx][ny] == "E":
                    answer.append(t+1)
                elif arr[nz][nx][ny] == "." and not visited[nz][nx][ny]:
                    dq.append((nz, nx, ny, t+1))
                    visited[nz][nx][ny] = True

    if len(answer) == 0:
        print("Trapped!")
    else:
        print(f"Escaped in {min(answer)} minute(s).")
