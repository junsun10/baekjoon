# 1로 만들기 ( 정답 )
# 알고리즘 : dp
# 세가지 경우의수 중 최솟값 선택

n = int(input())

if n == 1:
    print(0)

elif n <= 3:
    print(1)
else:
    dp = [0 for _ in range(n+1)]
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1

    for i in range(4, n+1):
        get_min = 10**6

        if dp[i-1] + 1 < get_min:
            get_min = dp[i-1] + 1

        if i % 2 == 0 and dp[i//2] + 1 < get_min:
            get_min = dp[i//2] + 1

        if i % 3 == 0 and dp[i//3] + 1 < get_min:
            get_min = dp[i//3] + 1

        dp[i] = get_min

    print(dp[n])
