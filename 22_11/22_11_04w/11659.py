# 구간 합 구하기 4
# 알고리즘 : 누적합


import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n)]
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = dp[i-1] + arr[i]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(dp[j-1])
    else:
        print(dp[j-1]-dp[i-2])
