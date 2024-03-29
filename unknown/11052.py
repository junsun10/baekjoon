# 카드 구매하기 ( 구글 정답 )

n = int(input())
arr = [0]+list(map(int, input().split()))
dp = [0 for i in range(n+1)]
dp[1] = arr[1]

for i in range(2, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + arr[j])

print(dp[n])
