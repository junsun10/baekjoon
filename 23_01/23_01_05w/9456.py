# 스티커 ( 구글 검색)


for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[1][i-1] + arr[0][i], dp[1][i-2] + arr[0][i])
        dp[1][i] = max(dp[0][i-1] + arr[1][i], dp[0][i-2] + arr[1][i])
    print(max(dp[0][-1], dp[1][-1]))
