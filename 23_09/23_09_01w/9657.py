# 돌 게임 ( 정답 )
# 알고리즘: dp

n = int(input())
dp = [0 for _ in range(n+1)]

if n == 1 or n == 3 or n == 4 or n == 5:
    print("SK")
elif n == 2:
    print("CY")
else:
    dp[0] = 0
    dp[1] = 1
    dp[2] = 0
    dp[3] = 1
    dp[4] = 1
    dp[5] = 1
    for i in range(5, n+1):
        if dp[i-1] == 0 or dp[i-3] == 0 or dp[i-4] == 0:
            dp[i] = 1

    if dp[n] == 1:
        print("SK")
    else:
        print("CY")
