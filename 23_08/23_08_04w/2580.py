# 스도쿠 ( 시간초과 )


def raw(x, y):
    visited = [False for _ in range(10)]
    for i in range(9):
        visited[arr[x][i]] = True
    available = []
    for i in range(1, 10):
        if visited[i] == False:
            available.append(i)
    return available


def column(x, y):
    visited = [False for _ in range(10)]
    for i in range(9):
        visited[arr[i][y]] = True
    available = []
    for i in range(1, 10):
        if visited[i] == False:
            available.append(i)
    return available


def square(x, y):
    i_x = x//3
    i_y = y//3
    visited = [False for _ in range(10)]
    for i in range(3):
        for j in range(3):
            visited[arr[3*i_x+i][3*i_y+j]] = True
    available = []
    for i in range(1, 10):
        if visited[i] == False:
            available.append(i)
    return available


def print_f(x, y, value):
    print(f"({x},{y}) value: {value}")
    for i in arr:
        print(*i)
    c = 0
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                c += 1
    print(f"count: {c}")
    print()


arr = [list(map(int, input().split())) for _ in range(9)]

count = 0
indexs = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            count += 1
            indexs.append((i, j))
while count > 0:
    for i in indexs:
        x, y = i[0], i[1]
        if arr[x][y] != 0:
            continue
        a_r = raw(x, y)
        a_c = column(x, y)
        a_s = square(x, y)
        # print(f"({x},{y}): {a_r}, {a_c}, {a_s}")
        if len(a_r) == 1:
            arr[x][y] = a_r[0]
            count -= 1
            # print("raw", a_r)
            # print_f(x, y, a_r[0])
        elif len(a_c) == 1:
            arr[x][y] = a_c[0]
            count -= 1
            # print("column", a_c)
            # print_f(x, y, a_c[0])
        elif len(a_s) == 1:
            arr[x][y] = a_s[0]
            count -= 1
            # print("square", a_s)
            # print_f(x, y, a_s[0])
        else:
            nums = [0 for _ in range(10)]
            for j in a_r:
                nums[j] += 1
            for j in a_c:
                nums[j] += 1
            for j in a_s:
                nums[j] += 1
            available = []
            for j in range(1, 10):
                if nums[j] == 3:
                    available.append(j)
            if len(available) == 1:
                arr[x][y] = available[0]
                count -= 1
                # print(a_r, a_c, a_s)
                # print_f(x, y, available[0])
            else:
                continue

# print()
for i in arr:
    print(*i)
