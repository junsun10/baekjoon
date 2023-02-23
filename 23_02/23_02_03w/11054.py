# 가장 긴 바이토닉 부분 수열 ( 정답 )
# 알고리즘 : dp
# 왼쪽에서 시작해서 증가하는 부분 수열 길이와
# 오른쪽에서 시작해서 증가하는 부분 수열 길이 각각 구한 뒤
# 두 경우의 합이 최대인 지점 선택

n = int(input())
arr = list(map(int, input().split()))

# 왼쪽에서 시작
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

# 오른쪽에서 시작
dp2 = [1 for _ in range(n)]
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[j] < arr[i] and dp2[i] < dp2[j] + 1:
            dp2[i] = dp2[j] + 1

answer = 0
for i in range(n):
    if dp[i] + dp2[i] - 1 > answer:
        answer = dp[i] + dp2[i] - 1

print(answer)
