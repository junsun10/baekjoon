# 미세먼지 안녕! ( 정답 )
# 알고리즘 : 구현
# 미세먼지 확산 후 공기청정기 작동

import copy

r, c, t = map(int, input().split())
arr = []
m = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
    temp = list(map(int, input().split()))
    arr.append(temp)
    if -1 in temp and len(m) == 0:
        m.append([i, temp.index(-1)])
        m.append([i+1, temp.index(-1)])

for _ in range(t):
    # 미세먼지 확산
    new_arr = [[0 for _ in range(c)] for _ in range(r)]
    new_arr[m[0][0]][m[0][1]] = -1
    new_arr[m[1][0]][m[1][1]] = -1
    for x in range(r):
        for y in range(c):
            if arr[x][y] != 0 and arr[x][y] != -1:
                new_arr[x][y] += arr[x][y]
                temp = arr[x][y]//5
                for i in range(4):
                    nx, ny = x + dx[i], y+dy[i]
                    if 0 <= nx < r and 0 <= ny < c:
                        if arr[nx][ny] != -1:
                            new_arr[nx][ny] += temp
                            new_arr[x][y] -= temp

    arr = copy.deepcopy(new_arr)
    # 위쪽 바람
    x, y = m[0]
    new_arr[x][y+1] = 0
    for i in range(1, c-1):
        new_arr[x][i+1] = arr[x][i]

    for i in range(1, x+1):
        new_arr[i-1][c-1] = arr[i][c-1]

    for i in range(1, c):
        new_arr[0][i-1] = arr[0][i]

    for i in range(0, x-1):
        new_arr[i+1][0] = arr[i][0]
    # 아래쪽 바람
    x, y = m[1]
    new_arr[x][y+1] = 0
    for i in range(1, c-1):
        new_arr[x][i+1] = arr[x][i]

    for i in range(x, r-1):
        new_arr[i+1][c-1] = arr[i][c-1]

    for i in range(1, c):
        new_arr[r-1][i-1] = arr[r-1][i]

    for i in range(x+2, r):
        new_arr[i-1][0] = arr[i][0]

    arr = copy.deepcopy(new_arr)


answer = 0
for i in range(r):
    answer += sum(arr[i])
print(answer+2)
