# 내리막 길 ( 정답 확인 )
# 알고리즘: dfs + DP
# 이미 방문한 지점에 대해 도달 가능한 경우의 수 dp를 사용해 중복 계산 제거

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
answer = 0
dp = [[0 for _ in range(n)] for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global answer

    if x == m-1 and y == n-1:
        return 1

    if dp[x][y] != 0:
        return dp[x][y]

    count = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if (0 <= nx < m) and (0 <= ny < n) and arr[x][y] > arr[nx][ny]:
            count += dfs(nx, ny)

    dp[x][y] = count
    return dp[x][y]


print(dfs(0, 0))
