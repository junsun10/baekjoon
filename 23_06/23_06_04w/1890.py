# 점프 ( 정담, 반례 검색 )
# 알고리즘 : dp


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] != 0:
            if i + arr[i][j] < n and arr[i][j] != 0:
                dp[i+arr[i][j]][j] += dp[i][j]
            if j + arr[i][j] < n and arr[i][j] != 0:
                dp[i][j+arr[i][j]] += dp[i][j]

print(dp[-1][-1])
