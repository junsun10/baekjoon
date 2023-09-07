# 이친수 ( 정답 )
# 알고리즘: dp

n = int(input())
dp = [[] for _ in range(n)]

dp[0] = [0, 1]

for i in range(1, n):
    dp[i] = [sum(dp[i-1]), dp[i-1][0]]

print(sum(dp[-1]))
