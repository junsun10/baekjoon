# 규칙적인 보스돌이 ( 정답 )
# 알고리즘: BFS
# 캐릭터의 공격력이 높은 순서대로 정렬
# 보스를 잡았을 경우와 잡지 않았을 경우를 나누어서 BFS를 돌림

from collections import deque

n, m, k = map(int, input().split())
d = [int(input()) for _ in range(n)]
boss = [list(map(int, input().split())) for _ in range(k)]

d.sort(key=lambda x: -x)

c_index = 0
answer = 0
while c_index < m:
    dq = deque()
    dq.append((0, 0, 0))
    max_money = 0
    while dq:
        money, time, index = dq.popleft()

        if index == k:
            if money > max_money:
                max_money = money
            continue

        dq.append((money, time, index+1))

        temp_time = 0
        if boss[index][0] % d[c_index] == 0:
            temp_time = boss[index][0] // d[c_index]
        else:
            temp_time = boss[index][0] // d[c_index] + 1

        if time + temp_time <= 900:
            dq.append((money+boss[index][1], time+temp_time, index+1))

    answer += max_money
    c_index += 1

print(answer)
