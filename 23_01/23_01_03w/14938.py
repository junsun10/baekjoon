# 서강 그라운드 ( 정답, 반례 검색 )
# 알고리즘 : bfs
# 이미 방분한 노드에 다른 더 짧은 경로로 도달하는 경우 있음
# 이미 방문한 경우 아이템 추가 x
# 문제의도 플로이드 워셜, 다익스트라

from collections import deque

n, m, r = map(int, input().split())
node = list(map(int, input().split()))
edge = [list(map(int, input().split())) for _ in range(r)]
answer = 0

for k in range(1, n+1):
    queue = deque()
    queue.append([k, 0])
    visited = [False for _ in range(n+1)]
    visited[k] = True
    temp_answer = node[k-1]
    while queue:
        now, length = queue.popleft()
        if length == m:
            continue
        for x, y, z in edge:
            if now == x and length+z <= m:
                queue.append([y, length+z])
                if not visited[y]:
                    temp_answer += node[y-1]
                visited[y] = True
            elif now == y and length+z <= m:
                queue.append([x, length+z])
                if not visited[x]:
                    temp_answer += node[x-1]
                visited[x] = True
    if temp_answer > answer:
        answer = temp_answer
print(answer)
