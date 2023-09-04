# 극장 좌석 ( 정답 )
# 알고리즘: dp
# dp를 사용하여 고정석이 없는 n개의 배열 경우의 수 계산
# 전체 좌석을 고정석으로 분리해 각 경우의 수를 dp에서 불러와서 곱함

n = int(input())
m = int(input())
arr = [int(input()) for _ in range(m)]

dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 2

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

answer = 1
before = 0
for i in arr:
    if i - before - 2 >= 0:
        answer = answer * dp[i-before-2]
    before = i

if n != before:
    answer = answer * dp[n-before-1]

print(answer)
