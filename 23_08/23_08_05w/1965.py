# 상자넣기 ( 정답 )
# 알고리즘: dp
# 이전까지 자신보다 크기가 작은 상자의 dp값 중 가장 큰 값 선택
# 작은 상자가 없으면 1

n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1, n):
    max_index = -1
    max_val = -1
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[j] > max_val:
                max_index = j
                max_val = dp[j]
    if max_index == -1:
        dp[i] = 1
    else:
        dp[i] = max_val + 1

print(max(dp))
