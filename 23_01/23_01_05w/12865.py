# 평범한 배낭 ( 정답 검색 )
# 알고리즘 : dp, 배낭 문제
# dp를 사용
# 1) 추가하려는 물건의 무게가 가방 크기보다 크면 이전 dp값 가져옴
# 2) max(현재 물건 가치 + dp[이전 물건][현재 가방 무게 - 현재 물건 무게], dp[이전 물건][현재 가방 무게])

n, k = map(int, input().split())
arr = [[0, 0]]
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w, v = arr[i]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])

print(dp[n][k])
