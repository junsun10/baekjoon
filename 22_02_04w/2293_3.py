# 동전 1 ( 시간초과 )

import sys

n,k = map(int,sys.stdin.readline().split())

arr = list(int(sys.stdin.readline()) for _ in range(n));
arr.sort(reverse=True)
# print(arr)

dp = [0 for _ in range(k+1)]


for i in range(arr[-1]):
    dp[i]=0
dp[arr[-1]]=1
# print(dp)


def dfs(x,now):
    print("now: (",x,",",now,")")
    

    if dp[now] != 0:
        print(dp)
        return dp[now]

    elif now < arr[-1]:
        # dp[now] = 0
        print(dp)
        return dp[now]
    
    elif x == n-1:
        if now%arr[x]!=0:
            print(dp)
            return dp[now]
        else:
            dp[now] += 1
            print(dp)
            return dp[now]

    
    elif now//arr[x] > 1:
        print("(",x+1,",",now,") (",x,",",now-arr[x],")")
        # dp[now] =  dfs(x+1,now) + dfs(x,now-arr[x])
        dp[now] = dfs(x,now-arr[x]) + dfs(x+1,now)
        return dp[now] 
    elif now//arr[x] == 1:
        print("(",x+1,",",now,") (",x+1,",",now-arr[x],")")
        # dp[now] = dfs(x+1,now) + dfs(x+1,now-arr[x])
        dp[now] = dfs(x+1,now-arr[x]) + dfs(x+1,now)
        return dp[now]
    elif now//arr[x] < 1:
        print("(",x+1,",",now,")")
        dp[now] = dfs(x+1,now)
        return dp[now]
    
    


print(dfs(0,k))
print(dp)