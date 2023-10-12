# 특정 거리의 도시 찾기 ( 정답 )
# 알고리즘: 다익스트라
# 다익스트라 알고리즘을 사용하여 최단거리 구함

import heapq

n, m, k, x = map(int, input().split())
# 경로를 2차원 배열로 만들었을 때 메모리 초과 발생
path = {}
for i in range(1, n+1):
    path[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    path[a].append([b, 1])

dist = [float(1e9) for _ in range(n+1)]
dist[x] = 0

heap = []
heapq.heappush(heap, [0, x])

while heap:
    distance, node = heapq.heappop(heap)

    if distance > dist[node]:
        continue

    for new_node, new_distance in path[node]:
        if distance + new_distance < dist[new_node]:
            dist[new_node] = distance + new_distance
            heapq.heappush(heap, [dist[new_node], new_node])

answer = []
for i in range(1, n+1):
    if dist[i] == k:
        answer.append(i)

if len(answer) > 0:
    for i in answer:
        print(i)
else:
    print(-1)
