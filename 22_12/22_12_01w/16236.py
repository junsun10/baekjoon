# 아기 상어 ( 정답 )
# 알고리즘 : BFS
# BFS 후 같은 거리에 있는 물고기를 조건에 맞춰 선택

from collections import deque

n = int(input())
arr = []
startPoint = (0, 0)  # 시작 위치
size = 2  # 상어 크기
count = 0  # 현재 크기에서 먹은 물고기 수
time = 0  # 정답 시간
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    for j in range(n):
        if temp[j] == 9:
            startPoint = (i, j)
            arr[i][j] = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
x, y = startPoint
while True:
    eat = False
    visited = [[False for _ in range(n)] for _ in range(n)]
    dq = deque()
    dq.append((x, y, 0))
    visited[x][y] = True
    temp = []  # 같은 거리에 갈 수 있는 물고기 위치 저장
    beforeT = 0  # 같은 거리 확인 위한 변수
    # BFS
    while dq:
        tx, ty, t = dq.popleft()
        # 새로운 이동거리 시작
        if len(temp) == 0:
            beforeT = t
        # 시간이 늘었고 먹을 수 있는 먹이가 있으면 탈출
        elif len(temp) > 0 and beforeT != t:
            break

        for i in range(4):
            nx, ny = tx + dx[i], ty + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if 0 < arr[nx][ny] < size:
                    temp.append([nx, ny, t])  # 먹이 위치 저장
                elif arr[nx][ny] == 0 or arr[nx][ny] == size:
                    dq.append((nx, ny, t+1))
                    visited[nx][ny] = True
                else:
                    continue

    # 조건에 맞는 먹이 위치 탐색
    if len(temp) > 0:
        x, y, t = temp[0][0], temp[0][1], temp[0][2]
        for tx, ty, tt in temp:
            if tx < x:
                x, y = tx, ty
            elif tx == x and ty < y:
                x, y = tx, ty
        arr[x][y] = 0  # 먹은 자리 0으로 초기화
        time += t+1  # 이동 시간 추가
        eat = True
        if count + 1 == size:
            count = 0
            size += 1
        else:
            count += 1

    # 종료 조건
    if not eat:
        print(time)
        break
