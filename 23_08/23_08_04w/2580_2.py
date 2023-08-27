# 스도쿠 ( 알고리즘 확인, 정답 확인 )
# 알고리즘: 백트래킹
# 0인 인덱스를 백트래킹으로 1~9까지 넣어본다

# 가로, 세로, 3*3 가능한지 확인
def possible(x, y, value):
    for i in range(9):
        if arr[x][i] == value:
            return False

    for i in range(9):
        if arr[i][y] == value:
            return False

    i_x, i_y = x//3, y//3
    for i in range(3):
        for j in range(3):
            if arr[3*i_x+i][3*i_y+j] == value:
                return False
    return True


def dfs(index):
    global end
    if end:
        return
    if index == count:
        for i in arr:
            print(*i)
        end = True
        return
    x, y = indexs[index]
    for i in range(1, 10):
        if possible(x, y, i):
            arr[x][y] = i

            dfs(index+1)

            arr[x][y] = 0


arr = [list(map(int, input().split())) for _ in range(9)]

count = 0
indexs = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            count += 1
            indexs.append((i, j))

end = False
dfs(0)
