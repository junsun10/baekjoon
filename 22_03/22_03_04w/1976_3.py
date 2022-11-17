# 여행가자

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
plan = list(map(int,input().split()))
answer = True
linked = arr[:]

def dfs(start,end):
    global visited, temp
    if arr[start][end] == 1:
        temp = True
        return
    else:
        for i in range(n):
            if arr[start][i] == 1 and visited[i] == False:
                visited[i] = True
                dfs(i,end)
                visited[i] = False
        


for i in range(m-1):
    if linked[plan[i]-1][plan[i+1]-1] == 1:
        continue
    else:
        visited = [False for _ in range(n)]
        visited[plan[i]-1] = True
        temp = False
        dfs(plan[i]-1,plan[i+1]-1)
        if temp:
            linked[plan[i]-1][plan[i+1]-1] = 1
            linked[plan[i+1]-1][plan[i]-1] = 1
            continue
        else:
            print("NO")
            answer = False
            break
if answer:
    print("YES")

# print(linked)


