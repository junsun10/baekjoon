# 폭탄 피하기 ( 시간초과 )

n, m, k = map(int, input().split())
bomb = [list(map(int, input().split())) for _ in range(k)]

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp[0][0] = 1

for i in range(n+1):
    for j in range(m+1):
        if i == 0 and j == 0:
            continue

        if [i, j] in bomb:
            continue

        temp = 0
        if i > 0:
            temp += dp[i-1][j]
        if j > 0:
            temp += dp[i][j-1]

        dp[i][j] = temp % 1000000007

print(dp[n][m])
