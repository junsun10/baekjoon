# 단지번호붙이기 ( 정답 )
# 알고리즘 : BFS
# BFS 돌리면서 단지 찾기

from collections import deque

sizeOfMap = int(input())
mapArr = [list(map(int, input())) for _ in range(sizeOfMap)]
visited = [[False for _ in range(sizeOfMap)] for _ in range(sizeOfMap)]
union = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(que):
    count = 1

    while que:
        nowX, nowY = que.popleft()

        for i in range(4):
            nx, ny = nowX+dx[i], nowY+dy[i]
            if nx >= 0 and nx < sizeOfMap and ny >= 0 and ny < sizeOfMap and mapArr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny))
                count += 1

    union.append(count)


for i in range(sizeOfMap):
    for j in range(sizeOfMap):
        if not visited[i][j]:
            visited[i][j] = True
            if mapArr[i][j] == 1:
                que = deque()
                que.append((i, j))
                bfs(que)

union.sort()
print(len(union))
for x in union:
    print(x)
