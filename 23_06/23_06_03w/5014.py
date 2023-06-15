# 스타트링크 ( 정답 )
# 알고리즘 : bfs

from collections import deque
# f: 전체 층, s: 현재 층, g: 목표 층, u: u층 위로, d: d층 아래로
f, s, g, u, d = map(int, input().split())

dq = deque()
visited = [False for _ in range(f+1)]

dq.append((s, 0))
answers = []

while dq:
    n, count = dq.popleft()

    if n == g:
        answers.append(count)

    else:
        if u > 0 and n+u <= f and not visited[n+u]:
            dq.append((n+u, count+1))
            visited[n+u] = True

        if d > 0 and n-d >= 1 and not visited[n-d]:
            dq.append((n-d, count+1))
            visited[n-d] = True

if len(answers) > 0:
    print(min(answers))
else:
    print("use the stairs")
