# 마인크래프트 ( 정답 )
# 알고리즘 : 구현
# 최고 높이부터 탐색

n, m, b = map(int, input().split())
world = []
answer_time = 500*500*256*3
answer_height = -1
for _ in range(n):
    world.append(list(map(int, input().split())))

height = 0
for i in range(n):
    height = max(max(world[i]), height)

while True:
    temp = 0
    time = 0
    inventory = b
    for i in range(n):
        for j in range(m):
            if world[i][j] > height:
                inventory += world[i][j] - height
                time += 2 * (world[i][j] - height)
            else:
                temp += height - world[i][j]
                time += 1 * (height - world[i][j])
    if temp > inventory:
        height -= 1
    else:
        if time < answer_time:
            answer_time = time
            answer_height = height
            height -= 1
        else:
            break

    if height == -1:
        break

print(answer_time, answer_height)
