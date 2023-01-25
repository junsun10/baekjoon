# 정수 삼각형 ( 정답 )
# 알고리즘 : dp
# 위에서 선택할 수 있는 두가지 위치 중 최댓값 선택

n = int(input())
arr = []
dp = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    temp = [0 for _ in range(i+1)]
    dp.append(temp)
dp[0][0] = arr[0][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + arr[i][0]
    dp[i][-1] = dp[i-1][-1] + arr[i][-1]

for i in range(2, n):
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

print(max(dp[-1]))
