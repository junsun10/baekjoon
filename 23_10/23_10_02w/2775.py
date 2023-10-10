# 부녀회장이 퇼테야 ( 정답 )
# 알고리즘: dp
# k층 n호부터 거꾸로 찾아감
# dp[x][y]가 이미 계산된 값이면 저장된 값 사용

dp = [[0 for _ in range(15)] for _ in range(15)]

for i in range(15):
    dp[0][i] = i
    dp[i][1] = 1


def f(x, y):
    if dp[x][y] != 0:
        return dp[x][y]

    else:
        dp[x][y] = f(x, y-1) + f(x-1, y)
        return dp[x][y]


for _ in range(int(input())):
    k = int(input())
    n = int(input())

    dp[k][n] = f(k, n)
    print(dp[k][n])
