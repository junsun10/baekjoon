# 동전 2 ( 정답 )
# 알고리즘 : dp

import sys
from collections import deque

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
coins.sort()

# 단일 종류의 동전으로만 만드는 경우 계산
dp = [100001 for _ in range(100001)]
for i in coins:
    temp = 1
    while temp*i < 100001:
        dp[temp*i] = min(temp, dp[temp*i])
        temp += 1

# i 보다 작은 값 두개를 합친 경우 계산
for i in range(1, k+1):
    count = 100001
    for j in range(1, i):
        count = min((dp[j]+dp[i-j]), count)
    dp[i] = min(dp[i], count)

# 불가능한 경우 확인
if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])
