# 벽장문의 이동 ( 정답 )
# 알고리즘: bfs, dp
# 가능한 경우의 수를 bfs에 추가
# dp로도 가능

from collections import deque

n = int(input())
open_door = list(map(int, input().split()))
c = int(input())
use = [int(input()) for _ in range(c)]
answer = 1000000
dq = deque()
dq.append((0, open_door, 0))

while dq:
    index, now_open, count = dq.popleft()
    if index == c:
        answer = min(answer, count)
    else:
        value = use[index]
        # 열려있는 경우
        if value in now_open:
            dq.append((index+1, now_open, count))
        else:
            temp = now_open.copy()
            temp_count = count
            temp_count += abs(now_open[0] - value)
            temp[0] = value
            dq.append((index+1, temp, temp_count))

            temp = now_open.copy()
            temp_count = count
            temp_count += abs(now_open[1] - value)
            temp[1] = value
            dq.append((index+1, temp, temp_count))

print(answer)
