# LCS ( 정답 )
# 알고리즘 : dp
# s1[i]와 s2[j]가 다른 경우
# 두 문자를 사용하기 전인 dp[i-1][j-1]에서 최장 부분수열 가져옴
# s1[i]와 s2[j]가 다른 경우
# dp[i-1][j]와 dp[i][j-1]중 긴 값 가져옴

s1 = input()
s2 = input()
max_len = 0
dp = [["" for _ in range(len(s2))] for _ in range(len(s1))]

# dp 초기화
# 첫 행 초기화
for i in range(len(s2)):
    # 문자가 같은 경우
    if s1[0] == s2[i]:
        dp[0][i] = s1[0]
    # 문자는 다르지만 이전 값이 있는경우
    elif i != 0 and dp[0][i-1] != "":
        dp[0][i] = dp[0][i-1]

# 첫 열 초기화
for i in range(len(s1)):
    if s1[i] == s2[0]:
        dp[i][0] = s1[i]
    elif i != 0 and dp[i-1][0] != "":
        dp[i][0] = dp[i-1][0]


for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + s1[i]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

        # 최대 길이 저장
        if len(dp[i][j]) > max_len:
            max_len = len(dp[i][j])

print(max_len)
