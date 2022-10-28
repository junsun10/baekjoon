# 테트로미노

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def dfs(x,y,c):
    global pol,val
    if c==3:
        return
    
    max_val = 0
    temp = 0
    
    for i in range(4):
        new_x = x+xy[i][0]
        new_y = y+xy[i][1]
        if 0<=new_x<=n-1 and 0<=new_y<=m-1 and arr[new_x][new_y] > max_val and (new_x,new_y) not in pol:
            max_val = arr[new_x][new_y]
            temp = i
    # print(max_val, temp)
    x = x+xy[temp][0]
    y = y+xy[temp][1]
    c += 1
    pol.append((x,y))
    val += max_val
    # print(pol)
    # print(val)
    return dfs(x,y,c)

xy = [[-1,0],[0,1],[1,0],[0,-1]]
answer = []
answer_val = []
for i in range(n):
    for j in range(m):
        pol = [(i,j)]
        val = arr[i][j]
        c = 0
        dfs(i,j,c)
        if pol not in answer:
            answer.append(pol)
            answer_val.append(val)

for i in range(len(answer)):
    print(answer[i])
print(answer_val)
print(max(answer_val))

        

        