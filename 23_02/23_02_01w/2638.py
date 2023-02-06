# 치즈 ( 정답 )
# 알고리즘 : bfs, 구현
# 치즈가 녹았을 때 내부 공간이 뚫리는지 확인해야 함
# 외부 공기0, 치즈1, 내부 공간2로 구분
# 전체 좌표를 돌면서 치즈가 녹을 수 있는지 확인
# 내부 공간이 뚫리면 처리후 다음 상태로 변환

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]


# 추가될 치즈인지 확인
def check(x, y, a):
    count = 0
    inside = []
    if arr[x][y] == 0 or arr[x][y] == 2:
        return False, None
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if a[nx][ny] == 0:
                count += 1
            elif a[nx][ny] == 2:
                inside.append([nx, ny])
    if count >= 2:
        return True, inside
    else:
        return False, None


# 뚫린 내부 공간 처리
def change_inside(i, j, a, b):
    queue = deque()
    queue.append((i, j))
    visited = [[i, j]]
    b[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if a[nx][ny] == 2 and not [nx, ny] in visited:
                    queue.append((nx, ny))
                    visited.append([nx, ny])
                    b[nx][ny] = 0
    return b


# 상태 변환
def dcopy(a):
    new_arr = []
    for i in range(n):
        new_arr.append(a[i][:])
    return new_arr


# 내부 공간 2로 초기화
queue = deque()
queue.append((0, 0))
visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True
while queue:
    x, y = queue.popleft()
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny]:
            if arr[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = True

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            arr[i][j] = 2

new_arr = dcopy(arr)

while True:
    change = False
    for i in range(1, n-1):
        temp = arr[i]
        for j in range(1, m-1):
            if temp[j] == 1:
                isplus, inside = check(i, j, arr)
                if isplus:
                    change = True
                    new_arr[i][j] = 0
                    for x, y in inside:
                        new_arr = change_inside(x, y, arr, new_arr)
    if not change:
        print(answer)
        break
    else:
        answer += 1
    arr = dcopy(new_arr)
