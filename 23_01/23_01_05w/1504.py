# 특정한 최단 경로 ( 정답, 알고리즘 검색 )
# 알고리즘 : 다익스트라
# 어느 정점을 먼저 지날지 두가지 경우의 수 확인

import heapq

n, e = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])
goal1, goal2 = map(int, input().split())
goals = [1, goal1, goal2]
visited = [[False for _ in range(n+1)] for _ in range(3)]
distances = [[1000000 for _ in range(n+1)] for _ in range(3)]

# 다익스트라 세번 진행
for i in range(3):
    queue = []
    heapq.heappush(queue, [0, goals[i]])
    distances[i][goals[i]] = 0
    visited[i][goals[i]] = True

    while queue:
        value, node = heapq.heappop(queue)

        for next_node, c in edges[node]:
            if distances[i][next_node] < value + c:
                continue
            if distances[i][next_node] > value + c:
                distances[i][next_node] = value + c
                heapq.heappush(queue, [distances[i][next_node], next_node])
            visited[i][next_node] = True

# 두가지 경우의 수 비교
answer1 = -1
if visited[0][goal1] and visited[1][goal2] and visited[2][n]:
    answer1 = distances[0][goal1] + distances[1][goal2] + distances[2][n]
answer2 = -1
if visited[0][goal2] and visited[2][goal1] and visited[1][n]:
    answer2 = distances[0][goal2] + distances[2][goal1] + distances[1][n]
if answer1 == -1:
    if answer2 == -1:
        print(-1)
    else:
        print(answer2)
else:
    if answer2 == -1:
        print(answer1)
    else:
        print(min(answer1, answer2))
