# LCS ( 정답 )
# 알고리즘: dp
# 문자를 하나씩 돌면서 dp를 사용해 이전 최댓값과 비교하면서 갱신

s1 = list(input())
s2 = list(input())

dp = [["" for _ in range(len(s2))] for _ in range(len(s1))]

check = False
for i in range(len(s1)):
    if check:
        dp[i][0] = s2[0]
    elif s1[i] == s2[0]:
        dp[i][0] = s2[0]
        check = True

check = False
for i in range(len(s2)):
    if check:
        dp[0][i] = s1[0]
    elif s2[i] == s1[0]:
        dp[0][i] = s1[0]
        check = True


for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        # 같은 문자일 경우
        if s1[i] == s2[j]:
            # s1[i], s2[j]를 쓰지않은 상태의 최댓값(dp[i-1][j-1])+1과 직전 최댓값(dp[i][j-1]) 비교
            if len(dp[i-1][j-1])+1 > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j-1] + s1[i]
            else:
                dp[i][j] = dp[i][j-1]
        # 다른 문자일 경우
        else:
            # 왼쪽과 위쪽의 최댓값 중 큰 값을 선택
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[-1][-1]))
