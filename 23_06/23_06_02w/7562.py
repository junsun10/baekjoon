# 나이트의 이동 ( 정답 )
# 알고리즘 : bfs

from collections import deque

t = int(input())

# 1시 방향부터 이동 가능한 위치
move = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

for _ in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    visited = [[False for _ in range(n)] for _ in range(n)]

    dq = deque()
    dq.append([start[0], start[1], 0])
    visited[start[0]][start[0]] = True

    while dq:
        x, y, c = dq.popleft()

        if x == end[0] and y == end[1]:
            print(c)
            break

        for i in range(8):
            nx, ny = x + move[i][0], y + move[i][1]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and not visited[nx][ny]:
                dq.append([nx, ny, c+1])
                visited[nx][ny] = True
