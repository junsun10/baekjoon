# 안전 영역 ( 정답 )
# 알고리즘 : 완전탐색, bfs
# 비 높이 0부터 100까지 완전탐색
# 각 높이에서 bfs로 안전 영역 개수 탐색

from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer_list = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 비 높이
for h in range(0, 101):
    temp = [[0 for _ in range(n)] for _ in range(n)]
    count_0 = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= h:
                temp[i][j] = 1
            else:
                count_0 += 1

    if count_0 == 0:
        answer_list.append(0)
        continue
    if count_0 == 1:
        answer_list.append(1)
        continue

    answer = 0
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 0:
                answer += 1
                dq = deque()
                dq.append((i, j))
                temp[i][j] = 2

                while dq:
                    x, y = dq.popleft()

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]

                        if nx >= 0 and nx < n and ny >= 0 and ny < n and temp[nx][ny] == 0:
                            dq.append((nx, ny))
                            temp[nx][ny] = 2

    answer_list.append(answer)

print(max(answer_list))
