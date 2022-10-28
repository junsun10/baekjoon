# 동전 1 ( 시간초과 )

import sys

n,k = map(int,sys.stdin.readline().split())

arr = list(int(sys.stdin.readline()) for _ in range(n));
arr.sort(reverse=True)
# print(arr)

dp = [-1 for _ in range(k+1)]


for i in range(arr[-1]):
    dp[i]=0
dp[arr[-1]]=1
print(dp)
def dfs(x,now):


    if now == arr[-1]:
        return dp[arr[-1]]
    elif now < arr[-1]:
        return 0

    elif dp[now] != -1:
        return dp[now]

    elif now-arr[x] < 0:
        return 0
    elif now-arr[x]==0:
        dp[now] = dfs(x+1,now)
        return dp[now]
    
    elif now//arr[x] > 1:
        print(x,now-arr[x])
        dp[now] = dfs(x,now-arr[x])
        return dp[now] 
    elif now//arr[x] == 1 and x+1<n-1:
        print(x,now,now-arr[x])
        dp[now] = dfs(x+1,now) + dfs(x+1,now-arr[x])
        return dp[now]
    


print(dfs(0,k))