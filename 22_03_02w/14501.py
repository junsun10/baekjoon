# 퇴사 ( 정답 )
# 1일부터 상담을 했을 경우와 안했을 경우를 각각 큐에 저장


import sys
from collections import deque

n = int(sys.stdin.readline())


arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# print(arr)

queue = deque()
queue.append((0,0))
answer = []

while queue:
    # print(queue)
    day, money = queue.popleft()
    if day == n:
        answer.append(money)
    elif day > n:
        continue
    else:
        # 상담을 했을 경우는 상담 끝나는 날, 보수 더해서 저장
        # 상담을 안했을 경우는 날짜+1, 보수 그대로 저장
        queue.append((day+arr[day][0],money+arr[day][1]))
        queue.append((day+1,money))

# print(answer)
print(max(answer))