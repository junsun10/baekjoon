# 동물원 ( 정답 )
# 알고리즘 : dp
# 점화식 dp[n] = dp[n-1]*2 + dp[n-2]

n = int(input())

dp = [1, 3]

if n == 1:
    print(3)
else:
    for i in range(2, n+1):
        new = dp[1] * 2 + dp[0]
        dp[0] = dp[1]
        dp[1] = new
    print(dp[-1] % 9901)
