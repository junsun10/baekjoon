# 뱀과 사다리 게임 ( 틀림 )
# dp로 구현 실패

n, m = map(int, input().split())
dp = [2**31-1 for _ in range(101)]
dp[0] = 100000
dp[1] = 0
ladder_from = []
ladder_to = []
snake_from = []
snake_to = []
visited = []
temp = []
for _ in range(n):
    x, y = map(int, input().split())
    temp.append([x, y])
temp.sort()
for x, y in temp:
    ladder_from.append(x)
    ladder_to.append(y)
temp = []
for _ in range(m):
    x, y = map(int, input().split())
    temp.append([x, y])
temp.sort()
for x, y in temp:
    snake_from.append(x)
    snake_to.append(y)
i = 1
while True:
    if i == 1:
        if i in ladder_from:
            dp[ladder_to[ladder_from.index(i)]] = min(
                dp[ladder_to[ladder_from.index(i)]], dp[i])
        elif i in snake_from and i not in visited:
            dp[snake_to[snake_from.index(i)]] = min(
                dp[snake_to[snake_from.index(i)]], dp[i])
            visited.append(i)
            i = snake_to[snake_from.index(i)]
    elif i <= 6:
        dp[i] = min(dp[i], min(dp[1:i]) + 1)
    else:
        dp[i] = min(dp[i], min(dp[i-6:i]) + 1)

    if i in ladder_from:
        dp[ladder_to[ladder_from.index(i)]] = min(
            dp[ladder_to[ladder_from.index(i)]], dp[i])
    elif i in snake_from and i not in visited:
        dp[snake_to[snake_from.index(i)]] = min(
            dp[snake_to[snake_from.index(i)]], dp[i])
        visited.append(i)
        i = snake_to[snake_from.index(i)]
    if i == 100:
        break
    else:
        i += 1
for i in range(1, 101):
    if i == 1:
        if i in ladder_from:
            dp[ladder_to[ladder_from.index(i)]] = min(
                dp[ladder_to[ladder_from.index(i)]], dp[i])
        elif i in snake_from and i not in visited:
            dp[snake_to[snake_from.index(i)]] = min(
                dp[snake_to[snake_from.index(i)]], dp[i])
            visited.append(i)
            i = snake_to[snake_from.index(i)]
    elif i <= 6:
        dp[i] = min(dp[i], min(dp[1:i]) + 1)
    else:
        dp[i] = min(dp[i], min(dp[i-6:i]) + 1)

print(dp[100])
# for i in range(1, 92, 10):
#     print((i-1), dp[i:i+10])
