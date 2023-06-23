# 효율적인 해킹 ( 정답 )
# 알고리즘 : bfs, dfs
# 신뢰 관계 딕셔너리를 만든 뒤 bfs

from collections import deque

n, m = map(int, input().split())

if n == 1:
    a, b = map(int, input().split())
    print(1)
else:
    # 신뢰 관계 딕셔너리 (value가 key를 신뢰)
    computers = {}
    for i in range(n+1):
        computers[i] = []

    for _ in range(m):
        a, b = map(int, input().split())
        computers[b] = computers[b] + [a]

    # 모든 컴퓨터에 대해 bfs
    answers = []
    for i in range(1, n+1):
        visited = [False for _ in range(n+1)]
        visited[i] = True
        dq = deque()
        dq.append(i)
        while dq:
            now = dq.popleft()

            for j in computers[now]:
                if not visited[j]:
                    visited[j] = True
                    dq.append(j)

        answers.append([visited.count(True)-1, i])

    answers.sort(key=lambda x: x[0], reverse=True)
    max_val = answers[0][0]
    for i in answers:
        if i[0] == max_val:
            print(i[1], end=" ")
        else:
            break
    print()
