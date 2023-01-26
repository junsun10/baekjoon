# 내려가기 ( 정답 )
# 알고리즘 : dp, 슬라이딩 윈도우
# 일반적인 dp 방식은 전체 입력에 대한 배열을 생성하므로 메모리 초과 발생
# 슬라이딩 윈도우 기법으로 1차원 배열을 갱신함

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [arr[0][0], arr[0][1], arr[0][2]]
answer = []
for i in range(1, n):
    temp = dp[:]
    dp[0] = max(temp[0], temp[1]) + arr[i][0]
    dp[1] = max(temp[0], temp[1], temp[2]) + arr[i][1]
    dp[2] = max(temp[1], temp[2]) + arr[i][2]
max_val = max(dp)

dp = [arr[0][0], arr[0][1], arr[0][2]]
for i in range(1, n):
    temp = dp[:]
    dp[0] = min(temp[0], temp[1]) + arr[i][0]
    dp[1] = min(temp[0], temp[1], temp[2]) + arr[i][1]
    dp[2] = min(temp[1], temp[2]) + arr[i][2]
min_val = min(dp)

print(max_val, min_val)
