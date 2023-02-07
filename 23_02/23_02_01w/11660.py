# 구간 합 구하기 5 ( 정답 )
# 알고리즘 : dp, 누적합
# 각 행별 누적합 구한 뒤 계산
# 2차원 누적합 한번에 하려면
# dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i][j]도 가능

import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
dp = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    dp[i][0] = arr[i][0]

for i in range(n):
    for j in range(1, n):
        dp[i][j] = dp[i][j-1] + arr[i][j]

for _ in range(m):
    answer = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1-1, x2):
        if y1 == 1:
            answer += dp[i][y2-1]
        else:
            answer += dp[i][y2-1] - dp[i][y1-2]
    print(answer)
