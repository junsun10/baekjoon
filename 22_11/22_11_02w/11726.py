# 2 x n 타일링 ( 정답 )
# 알고리즘 : DP
# n번째 경우의수는 n-1번째 + n-2번째인 규칙 찾기

n = int(input())

dp = [0, 1, 2]

for i in range(3, n+1):
    dp.append((dp[i-1] + dp[i-2]) % 10007)

print(dp[n])
