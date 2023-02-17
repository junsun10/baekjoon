# 가장 긴 증가하는 부분 수열 ( 정답 )
# 알고리즘 : dp
# 자신보다 작은 이전 값들의 dp값 중 최댓값 선택

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(i):
        if arr[i] > arr[j] and dp[j]+1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
