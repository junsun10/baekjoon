# Four Squres ( 구글정답 )
# 알고리즘 : dp
# 자신의 수(i)에서 그보다 작은 수(j)의 제곱수를 뺀 것의
# 최소(min(min_value, dp[i - (j**2)]))를 구하고 거기에 한개를 더해준다.

from math import *
from itertools import product

n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    min_value = 4
    j = 1
    while (j**2) <= i:
        min_value = min(min_value, dp[i - (j**2)])
        j += 1
    # dp[i-(j**2)]개 + j**2 1개
    dp.append(min_value + 1)

print(dp[n])
