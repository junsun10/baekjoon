# 계단 오르기 ( 알고리즘 검색, 정답 검색 )
# 알고리즘 : DP
# dp 공식을 찾지 못했음

numOfStairs = int(input())
stairsArr = [int(input()) for _ in range(numOfStairs)]
dp = [stairsArr[0], stairsArr[0]+stairsArr[1],
      max(stairsArr[0], stairsArr[1])+stairsArr[2]]

for i in range(3, numOfStairs):
    dp.append(max(dp[i-2] + stairsArr[i], dp[i-3] +
              stairsArr[i] + stairsArr[i - 1]))

print(dp[-1])
