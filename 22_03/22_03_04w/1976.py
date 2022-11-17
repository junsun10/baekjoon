# 여행가자

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
plan = list(map(int,input().split()))
answer = True
linked = []

def dfs(start,end):
    global visited
    visited[start] = True
    if arr[start][end] == 1:
        return True
    for i in range(n):
        if arr[start][i] == 1 and visited[i] == False:
            visited[i] = True
            dfs(i,end)
            visited[i] = False
        else:
            continue
    return False


for i in range(0,m-1):
    visited = [False for _ in range(n)]
    if dfs(plan[i]-1,plan[i+1]-1):
        # print(plan[i],"to",plan[i+1],"linked")
        continue
    else:
        print("NO")
        answer = False
        break

if answer == True:
    print("YES")
