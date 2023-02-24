# 파이프 옮기기 1 ( 70% 시간초과 )
# 알고리즘 : bfs
# bfs로는 시간초과 발생

from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 파이프의 상태
# 가로: 0, 세로: 1, 대각선: 2

answer = 0

queue = deque()
queue.append((0, 0, 0, 0, 1))

while queue:
    s, x1, y1, x2, y2 = queue.popleft()

    if x2 == n-1 and y2 == n-1:
        answer += 1
        continue

    if s == 0:
        if y2+1 < n and arr[x2][y2+1] == 0:
            queue.append((0, x2, y2, x2, y2+1))

            if x2+1 < n and arr[x2+1][y2] == 0 and arr[x2+1][y2+1] == 0:
                queue.append((2, x2, y2, x2+1, y2+1))

    elif s == 1:
        if x2+1 < n and arr[x2+1][y2] == 0:
            queue.append((1, x2, y2, x2+1, y2))

            if y2+1 < n and arr[x2][y2+1] == 0 and arr[x2+1][y2+1] == 0:
                queue.append((2, x2, y2, x2+1, y2+1))

    else:
        if y2+1 < n and arr[x2][y2+1] == 0:
            queue.append((0, x2, y2, x2, y2+1))

        if x2+1 < n and arr[x2+1][y2] == 0:
            queue.append((1, x2, y2, x2+1, y2))

            if y2+1 < n and arr[x2][y2+1] == 0 and arr[x2+1][y2+1] == 0:
                queue.append((2, x2, y2, x2+1, y2+1))

print(answer)
