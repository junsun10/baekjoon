# 연결 요소의 개수 ( 정답 )
# 알고리즘 : BFS
# 연결된 노드들 BFS로 탐색

from collections import deque

n, m = map(int, input().split())
arr = [[False for _ in range(n+1)] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
groups = []

for _ in range(m):
    x, y = map(int, input().split())
    arr[x][y] = True
    arr[y][x] = True

for i in range(1, n+1):
    if not visited[i]:
        dq = deque()
        dq.append(i)
        visited[i] = True
        temp = [i]
        while dq:
            x = dq.popleft()
            for j in range(1, n+1):
                if arr[x][j] == True and not visited[j]:
                    dq.append(j)
                    temp.append(j)
                    visited[j] = True
        groups.append(temp)

print(len(groups))
