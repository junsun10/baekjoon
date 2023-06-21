# 1로 만들기 2 ( 정답 )
# 알고리즘 : dp, 그래프
# dp로 갈 수 있는 세가지 경우의 수 중 최소값 선택
# 경로 출력을 위해 dp 배열에 어느 숫자로 이동했는지 저장

n = int(input())
dp = [[10**6, -1] for _ in range(10**6+1)]

dp[1] = [0, -1]
dp[2] = [1, 1]
dp[3] = [1, 1]

for i in range(4, n+1):
    temp1, temp2, temp3 = 10**6, 10**6, 10**6
    if i % 3 == 0:
        temp1 = dp[i//3][0] + 1
    if i % 2 == 0:
        temp2 = dp[i//2][0] + 1

    temp3 = dp[i-1][0] + 1

    answer = min(temp1, temp2, temp3)

    if answer == temp1:
        dp[i] = [temp1, i//3]
    elif answer == temp2:
        dp[i] = [temp2, i//2]
    else:
        dp[i] = [temp3, i-1]


print(dp[n][0])
temp = n
print(temp, end=" ")
while True:
    if dp[temp][1] != -1:
        print(dp[temp][1], end=" ")
        temp = dp[temp][1]
    else:
        print()
        break
