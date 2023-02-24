# 트리의 지름 ( 정답 )
# 알고리즘 : bfs
# 각 노드를 시작으로 bfs 실행해 가중치 합의 최대 계산

from collections import deque

n = int(input())
edges = [[] for _ in range(n+1)]

for i in range(n-1):
    x, y, w = map(int, input().split())
    edges[x].append([y, w])
    edges[y].append([x, w])

answer = 0

# 모든 노드 실행
for i in range(1, n+1):
    # bfs
    visited = [False for _ in range(n+1)]
    queue = deque()
    queue.append((i, 0))
    visited[i] = True

    while queue:
        now, distance = queue.popleft()

        for to, w in edges[now]:
            if not visited[to]:
                queue.append((to, distance+w))
                visited[to] = True
                if distance + w > answer:
                    answer = distance + w

print(answer)
