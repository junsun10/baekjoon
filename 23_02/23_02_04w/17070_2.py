# 파이프 옮기기 1 ( 정답, 알고리즘 확인 )
# 알고리즘 : dp
# 파이프의 상태에 따른 경우의 수를 따로 저장(dp 배열)
# 확인하려는 위치로 올 수 있는 경우의 수를 파이프의 상태에 따라 각각 계산(move 배열)

from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 파이프 상태 index
# 가로: 0, 세로: 1, 대각선: 2

dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][0] = [1, 1, 1]
dp[0][1] = [1, 1, 1]

# 각 상태의 파이프가 도달할 수 있는 위치
move = [[[False, False, False] for _ in range(n)] for _ in range(n)]
move[0][0] = [True, True, True]
move[0][1] = [True, True, True]

answer = 0

for i in range(n):
    for j in range(2, n):

        if arr[i][j] == 0:

            # 가로 -> 가로
            if move[i][j-2][0] and move[i][j-1][0]:
                move[i][j][0] = True
                dp[i][j][0] += dp[i][j-1][0]

            # 가로 -> 대각
            if move[i-1][j-2][0] and move[i-1][j-1][0] and arr[i-1][j] == 0 and arr[i][j-1] == 0:
                move[i-1][j-1][2] = True
                move[i][j][2] = True
                dp[i][j][2] += dp[i-1][j-1][0]

            # 세로 -> 세로
            if move[i-2][j][1] and move[i-1][j][1]:
                move[i][j][1] = True
                dp[i][j][1] += dp[i-1][j][1]

            # 세로 -> 대각
            if move[i-2][j-1][1] and move[i-1][j-1][1] and arr[i-1][j] == 0 and arr[i][j-1] == 0:
                move[i-1][j-1][2] = True
                move[i][j][2] = True
                dp[i][j][2] += dp[i-1][j-1][1]

            # 대각 -> 가로
            if move[i-1][j-2][2] and move[i][j-1][2]:
                move[i][j-1][0] = True
                move[i][j][0] = True
                dp[i][j][0] += dp[i][j-1][2]

            # 대각 -> 세로
            if move[i-2][j-1][2] and move[i-1][j]:
                move[i-1][j][1] = True
                move[i][j][1] = True
                dp[i][j][1] += dp[i-1][j][2]

            # 대각 -> 대각
            if move[i-2][j-2][2] and move[i-1][j-1] and arr[i-1][j] == 0 and arr[i][j-1] == 0:
                move[i][j][2] = True
                dp[i][j][2] += dp[i-1][j-1][2]

print(sum(dp[n-1][n-1]))
