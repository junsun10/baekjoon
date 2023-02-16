# N-Queen ( 정답 )
# 알고리즘 : 백트래킹
# 백트래킹을 통해 경우의수 모두 탐색

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
count = 0
answer = []


def change(x, y):
    arr[x][y] = 1
    for i in range(1, x+1):
        arr[x-i][y] += 1
    for i in range(1, n-x):
        arr[x+i][y] += 1
    for i in range(1, y+1):
        arr[x][y-i] += 1
        # 왼쪽 위
        if x-i >= 0:
            arr[x-i][y-i] += 1
        # 왼쪽 아래
        if x+i < n:
            arr[x+i][y-i] += 1
    for i in range(1, n-y):
        arr[x][y+i] += 1
        # 오른쪽 위
        if x-i >= 0:
            arr[x-i][y+i] += 1
        # 오른쪽 아래
        if x+i < n:
            arr[x+i][y+i] += 1


def unchange(x, y):
    arr[x][y] -= 1
    for i in range(1, x+1):
        arr[x-i][y] -= 1
    for i in range(1, n-x):
        arr[x+i][y] -= 1
    for i in range(1, y+1):
        arr[x][y-i] -= 1
        # 왼쪽 위
        if x-i >= 0:
            arr[x-i][y-i] -= 1
        # 왼쪽 아래
        if x+i < n:
            arr[x+i][y-i] -= 1
    for i in range(1, n-y):
        arr[x][y+i] -= 1
        # 오른쪽 위
        if x-i >= 0:
            arr[x-i][y+i] -= 1
        # 오른쪽 아래
        if x+i < n:
            arr[x+i][y+i] -= 1


def dfs(x):
    global count

    if len(answer) == n:
        count += 1
        return

    for j in range(n):
        if arr[x+1][j] == 0:
            answer.append((x+1, j))
            change(x+1, j)
            dfs(x+1)
            answer.pop()
            unchange(x+1, j)


dfs(-1)
print(count)
