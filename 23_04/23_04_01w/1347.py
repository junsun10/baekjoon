# 미로 만들기 ( 정답 )
# 알고리즘 : 구현

n = int(input())
log = list(input())

w = 1  # 0,1,2,3 동남서북
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
x, y = 0, 0
m = [[0, 0]]

for i in log:
    if i == "R":
        w = (w+1) % 4
    elif i == "L":
        w = (w+3) % 4
    else:
        x += move[w][0]
        y += move[w][1]
        m.append([x, y])

height = max(m, key=lambda x: x[0])[0]-min(m, key=lambda x: x[0])[0]+1
width = max(m, key=lambda x: x[1])[1]-min(m, key=lambda x: x[1])[1]+1
min_height = min(m, key=lambda x: x[0])[0]
min_width = min(m, key=lambda x: x[1])[1]
answer = [["#" for _ in range(width)] for _ in range(height)]

for i, j in m:
    if min_height < 0 and min_width < 0:
        answer[i-min_height][j-min_width] = "."
    elif min_height < 0:
        answer[i-min_height][j] = "."
    else:
        answer[i][j-min_width] = "."

for i in answer:
    for j in i:
        print(j, end="")
    print()
