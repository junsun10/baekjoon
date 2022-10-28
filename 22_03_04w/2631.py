# 줄세우기 ( 구글정답 )

# 증가하는 최장 부분수열 구하기
# n^2

n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [1 for _ in range(n+1)]

for i in range(1,n):
    for j in range(0,i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i],dp[j]+1)

answer = n - max(dp)
print(answer)

