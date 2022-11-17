# 연구소 ( 정답 )
# 알고리즘: BFS, 완전탐색
# 벽을 세울 수 있는 모든 경우의 수 완전탐색
# 바이러스 좌표를 모두 큐에 넣은 뒤 bfs

from collections import deque

n, m = map(int, input().split())
input_arr = [list(map(int, input().split())) for _ in range(n)]
# 빈칸 좌표
empty_index = []
# 바이러스 좌표
virus_index = []
answer_list = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    visited = [[False for _ in range(m)] for _ in range(n)]
    # 바이러스가 퍼진 칸
    count = 0
    dq = deque()
    # 바이러스 모두 큐에 추가
    for i in virus_index:
        dq.append(i)
        visited[i[0]][i[1]] = True

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and input_arr[nx][ny] == 0 and not visited[nx][ny]:
                count += 1
                dq.append((nx, ny))
                visited[nx][ny] = True
    return count


# 빈칸, 바이러스 좌표 검색
for i in range(n):
    for j in range(m):
        if input_arr[i][j] == 0:
            empty_index.append((i, j))
        elif input_arr[i][j] == 2:
            virus_index.append((i, j))

# 벽을 세울 수 있는 모든 경우의 수 완전탐색
for i in range(len(empty_index)-2):
    for j in range(i+1, len(empty_index)-1):
        for k in range(j+1, len(empty_index)):
            input_arr[empty_index[i][0]][empty_index[i][1]] = 1
            input_arr[empty_index[j][0]][empty_index[j][1]] = 1
            input_arr[empty_index[k][0]][empty_index[k][1]] = 1
            count = bfs()
            # 안전한 공간의 개수
            answer_list.append(len(empty_index)-count-3)
            input_arr[empty_index[i][0]][empty_index[i][1]] = 0
            input_arr[empty_index[j][0]][empty_index[j][1]] = 0
            input_arr[empty_index[k][0]][empty_index[k][1]] = 0

print(max(answer_list))
