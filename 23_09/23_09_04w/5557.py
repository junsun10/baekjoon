# 1학년 ( 정답 )
# 알고리즘: dp
# 각 위치에서 0 ~ 20을 만들 수 있는 경우의 수를 dp에 저장
# 직전 위치에서 만들 수 있는 수 중에서 현재 위치 값을 더하고 뺐을때 가능한 경우의 수 탐색

n = int(input())
arr = list(map(int, input().split()))

dp = [[0 for _ in range(21)] for _ in range(n-1)]
# 첫번째 숫자 위치에 경우의 수 1
dp[0][arr[0]] = 1

# 두번째부터 n-1까지
for i in range(1, n-1):
    # 0 ~ 20
    for j in range(21):
        # 직전에 만들 수 없는 수이면 통과
        if dp[i-1][j] == 0:
            continue
        else:
            temp = j + arr[i]
            # j와 현재 값을 더했을 때 20이하면 현재 dp의 temp 위치에 직전 dp에서 j를 만들 수 있는 경우의 수 더함
            if temp <= 20:
                dp[i][temp] += dp[i-1][j]
            # 뺐을때 양수이면 위 조건문과 동일하게 수행
            temp = j - arr[i]
            if temp >= 0:
                dp[i][temp] += dp[i-1][j]

# n-1번째 dp에서 마지막 숫자의 인덱스 값을 읽어옴
print(dp[-1][arr[-1]])
