# 트리의 부모 찾기 ( 정답 )
# 알고리즘 : bfs
# 루트 노드인 1부터 시작해서 bfs 돌면서 부모 자식 관계 확인

from collections import deque

n = int(input())
arr = [[]for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

parents = [-1 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
visited[1] = True
queue = deque()

for i in range(len(arr[1])):
    queue.append((1, arr[1][i]))
    parents[arr[1][i]] = 1
    visited[arr[1][i]] = True

while queue:
    p, c = queue.popleft()

    for i in range(len(arr[c])):
        if not visited[arr[c][i]]:
            queue.append((c, arr[c][i]))
            parents[arr[c][i]] = c
            visited[arr[c][i]] = True

for i in range(2, n+1):
    print(parents[i])
