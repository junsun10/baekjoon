# 숨바꼭질 3 ( 정답 )
# 알고리즘 : bfs
# 이동한 위치가 이전보다 빨리 도착하면 갱신

from collections import deque

n, k = map(int, input().split())
if n >= k:
    print(n-k)
else:
    distance = [100001 for _ in range(200002)]
    queue = deque()
    queue.append((0, n))
    answer = []

    while queue:
        count, now = queue.popleft()
        if now == k:
            answer.append(count)
        if count > distance[now]:
            continue

        if now*2 < k*2 and now*2 > -(k*2) and distance[now*2] > count:
            queue.append((count, now*2))
            distance[now*2] = count

        if now+1 < k*2 and distance[now+1] > count + 1:
            queue.append((count+1, now+1))
            distance[now+1] = count + 1

        if now-1 >= 0 and distance[now-1] > count + 1:
            queue.append((count+1, now-1))
            distance[now-1] = count + 1

    print(min(answer))
