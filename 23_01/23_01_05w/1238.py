# 파티 ( 정답 )
# 알고리즘 : 다익스트라
# 다익스트라 알고리즘을 반복해
# 각 마을에서 다른 마을까지의 최단거리 계산
# 구한 거리 배열을 사용해 학생별 파티장까지의 왕복 거리 계산

import heapq

n, m, x = map(int, input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])

# 각 마을에서 다른 마을까지의 최단거리 계산
distances = [[100*(n+1) for _ in range(n+1)] for _ in range(n+1)]
for start in range(1, n+1):
    queue = []
    heapq.heappush(queue, (0, start))
    distances[start][start] = 0

    while queue:
        distance, now = heapq.heappop(queue)

        if distance > distances[start][now]:
            continue

        for to, d in arr[now]:
            if distances[start][to] > distance + d:
                distances[start][to] = distance + d
                heapq.heappush(queue, (distance+d, to))

# 학생별 파티장까지 왕복 거리 계산
answer = []
for i in range(1, n+1):
    answer.append(distances[i][x] + distances[x][i])
print(max(answer))
