# 경비행기

import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

arr = [(0,0)]
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    arr.append((x,y))
arr.sort()
arr.append((10000,10000))
print(arr)

w = [[0 for _ in range(n+2)] for _ in range(n+2)]


for i in range(n+2):
    for j in range(n+2):
        if ((arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2)**(1/2)%10 != 0:
            w[i][j] = ((arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2)**(1/2)//10+1
            w[j][i] = ((arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2)**(1/2)//10+1
        else:
            w[i][j] = ((arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2)**(1/2)//10
            w[j][i] = ((arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2)**(1/2)//10

# for i in range(n+2):
#     print(w[i])

# print(arr.index((10000,10000)))

def bfs(mid):
    visited[0] = True
    queue = deque()
    queue.append((0,0,0))
    while queue:
        print(queue)
        now_x, now_y, now_c = queue.popleft()
        if now_x == 10000 and now_y == 10000 and now_c <= k:
            return True
        if now_c > k and now_x != 10000 and now_y != 10000:
            return False
        for x,y in arr:
            if not visited[arr.index((x,y))] and w[arr.index((now_x,now_y))][arr.index((x,y))] <= mid and now_c < k:
                queue.append((x,y,now_c+1))
                # visited[arr.index((x,y))] = True
    
    return False


low, high = 0, 20000
while low <= high:
    visited = [False for _ in range(n+2)]
    mid = (low+high)//2
    if bfs(mid):
        high = mid - 1
    else:
        low = mid + 1
    print(low,mid,high)

print(high)
