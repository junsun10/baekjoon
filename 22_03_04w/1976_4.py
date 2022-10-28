# 여행가자

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
plan = list(map(int,input().split()))
answer = True
linked = arr[:]
union = []

def dfs(start,end):
    global visited, temp, linked, union
    if arr[start][end] == 1:
        temp = True
        for i in range(len(union)):
            linked[union[i]][end] = 1
            linked[end][union[i]] = 1
        return
    else:
        for i in range(n):
            if arr[start][i] == 1 and visited[i] == False:
                visited[i] = True
                for i in range(len(union)):
                    linked[union[i]][end] = 1
                    linked[end][union[i]] = 1
                union.append(i)
                dfs(i,end)
                visited[i] = False
                union = union[:-1]
        


for i in range(m-1):
    union = []
    if linked[plan[i]-1][plan[i+1]-1] == 1:
        continue
    else:
        visited = [False for _ in range(n)]
        visited[plan[i]-1] = True
        temp = False
        union = [plan[i]-1]
        dfs(plan[i]-1,plan[i+1]-1)
        if temp:
            continue
        else:
            print("NO")
            answer = False
            break
if answer:
    print("YES")

print(linked)


