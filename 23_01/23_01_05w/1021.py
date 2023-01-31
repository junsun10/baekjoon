# 회전하는 큐 ( 정답 )
# 알고리즘 : 자료구조, 덱

from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
queue = deque()
for i in range(n):
    queue.append(i+1)

for i in arr:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        # 왼쪽으로 돌릴지 오른쪽으로 돌릴지 선택
        index_i = queue.index(i)
        if index_i < len(queue)//2 + 1:
            queue.rotate(-1)
            answer += 1
        else:
            queue.rotate()
            answer += 1

print(answer)
