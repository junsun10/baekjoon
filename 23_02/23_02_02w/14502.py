# 연구소 ( 정답 )
# 알고리즘 : 백트래킹, bfs
# 1) 벽을 세울 위치의 모든 경우의 수를 백트래킹을 통해 구한다
# 2) 각 경우의 수에서 bfs를 통해 안전 영역의 크기를 구한다

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]


# 벽을 세울 위치 선택
def pick_three(x):
    if len(temp) == 3:
        new_walls.append(temp[:])
        return
    for i in range(x+1, len(empty)):
        temp.append(empty[i])
        pick_three(i)
        temp.pop()


virus = []
count_virus = 0
wall = []
count_wall = 0
empty = []
count_empty = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            empty.append((i, j))
            count_empty += 1
        elif arr[i][j] == 1:
            wall.append((i, j))
            count_wall += 1
        else:
            virus.append((i, j))
            count_virus += 1

# 벽을 세울 위치들
new_walls = []
temp = []
pick_three(-1)
answer = -1

# 모든 경우의 수 실행
for x, y, z in new_walls:
    change = 0
    arr[x[0]][x[1]] = 1
    arr[y[0]][y[1]] = 1
    arr[z[0]][z[1]] = 1

    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque()
    for i in virus:
        queue.append((i[0], i[1]))

    while queue:
        nx, ny = queue.popleft()

        for i, j in d:
            dx, dy = nx+i, ny+j

            if dx >= 0 and dx < n and dy >= 0 and dy < m and arr[dx][dy] == 0 and not visited[dx][dy]:
                queue.append((dx, dy))
                visited[dx][dy] = True
                change += 1
    if count_empty - 3 - change > answer:
        answer = count_empty - 3 - change

    arr[x[0]][x[1]] = 0
    arr[y[0]][y[1]] = 0
    arr[z[0]][z[1]] = 0

print(answer)
