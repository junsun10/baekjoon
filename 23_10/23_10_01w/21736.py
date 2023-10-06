# 헌내기는 친구가 필요해 ( 정답 )
# 알고리즘: bfs
# 이동 가능한 경로 bfs 진행

from collections import deque

n, m = map(int, input().split())
arr = []
start = []
for i in range(n):
    temp = list(input())
    arr.append(temp)
    if "I" in temp:
        start = [i, temp.index("I")]
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

dq = deque()
dq.append((start[0], start[1]))
visited[start[0]][start[1]] = True

while dq:
    x, y = dq.popleft()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if (0 <= nx < n) and (0 <= ny < m):
            if arr[nx][ny] == "O" and not visited[nx][ny]:
                dq.append((nx, ny))
                visited[nx][ny] = True
            elif arr[nx][ny] == "P" and not visited[nx][ny]:
                dq.append((nx, ny))
                answer += 1
                visited[nx][ny] = True

if answer != 0:
    print(answer)
else:
    print("TT")
