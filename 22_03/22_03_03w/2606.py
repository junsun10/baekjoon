# 바이러스 ( 정답 )

import sys
from collections import deque

n = int(sys.stdin.readline())
link = int(sys.stdin.readline())

arr = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(link):
    x,y = map(int,sys.stdin.readline().split())
    arr[x][y] = 1
    arr[y][x] = 1

queue = deque()
queue.append(1)
visited = [False for _ in range(n+1)]
visited[1] = True

while queue:
    now = queue.popleft()
    for i in range(n+1):
        if visited[i] == False and arr[now][i] == 1:
            queue.append(i)
            visited[i] = True

answer = 0
for i in visited:
    if i == True:
        answer += 1

print(answer-1)