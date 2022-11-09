# 유기농 배추 ( 정답 )
# 알고리즘 : BFS
# 배추위치를 기록한 뒤 bfs


from collections import deque

t = int(input())
width, height, locationNum = 0, 0, 0
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find():
    global answer, width, height, locationNum
    width, height, locationNum = map(int, input().split())
    mapArr = [[0 for _ in range(width)] for _ in range(height)]
    for _ in range(locationNum):
        x, y = map(int, input().split())
        mapArr[y][x] = 1
    visited = [[False for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            if not visited[i][j] and mapArr[i][j] == 1:
                que = deque()
                que.append((i, j))
                visited[i][j] = True
                answer += 1
                bfs(que, visited, mapArr)


def bfs(que, visited, mapArr):
    global width, height
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < height and 0 <= ny < width and not visited[nx][ny] and mapArr[nx][ny] == 1:
                que.append((nx, ny))
                visited[nx][ny] = True


for _ in range(t):
    answer = 0
    find()
    print(answer)
