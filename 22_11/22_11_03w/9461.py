# 파도반 수열 ( 정답 )
# 알고리즘 : DP
# 규칙 찾아서 DP

t = int(input())

for _ in range(t):
    n = int(input())

    dp = [1, 1, 1, 2, 2]

    for i in range(5, n):
        dp.append(dp[i-1] + dp[i-5])

    print(dp[n-1])
