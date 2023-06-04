# 포도주 시식 ( 정답 )
# 알고리즘: dp
# 현재 위치까지의 최대값을 구하는 경우의 수 세가지 계산
# 1) i-2, i 선택
# 2) i-1, i 선택
# 3) i-2, i-1 선택

n = int(input())
list = [int(input()) for _ in range(n)]

if n == 1:
    print(list[0])
else:
    dp = [0 for _ in range(n)]
    dp[0] = list[0]
    dp[1] = list[0] + list[1]

    for i in range(2, n):
        if i == 2:
            dp[i] = max(dp[i-2]+list[i], list[i-1]+list[i], dp[i-1])
        else:
            dp[i] = max(dp[i-2]+list[i], dp[i-3]+list[i-1]+list[i], dp[i-1])

    print(max(dp))
