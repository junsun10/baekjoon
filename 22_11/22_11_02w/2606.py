# 바이러스 ( 정답 )
# 알고리즘 : BFS
# BFS 돌면서 카운팅

from collections import deque

numOfComputers = int(input())
numOfEdges = int(input())
edgesArr = [list(map(int, input().split())) for _ in range(numOfEdges)]
visited = [False for _ in range(numOfComputers + 1)]
count = 0

que = deque()
que.append(1)
visited[1] = True

while que:
    nowNode = que.popleft()
    for x, y in edgesArr:
        if nowNode == x and not visited[y]:
            que.append(y)
            visited[y] = True
            count += 1
        elif nowNode == y and not visited[x]:
            que.append(x)
            visited[x] = True
            count += 1

print(count)
