# 알파벳 ( 정답 )
# 알고리즘: 백트래킹
# 방문한 알파벳을 저장한 뒤 상하좌우 방문
# 방문한 알파벳 저장시 dict 사용시 시간초과 발생
# 시간제한이 조금 빡빡한 문제

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시간초과
# visited = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0,
#            "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}

visited = [0]*26
answer = 1


def dfs(x, y, count):
    global answer

    answer = max(answer, count)
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < r and 0 <= ny < c and visited[ord(arr[nx][ny])-65] == 0:
            visited[ord(arr[nx][ny])-65] = 1
            dfs(nx, ny, count+1)
            visited[ord(arr[nx][ny])-65] = 0


visited[ord(arr[0][0])-65] = 1
dfs(0, 0, 1)
print(answer)
