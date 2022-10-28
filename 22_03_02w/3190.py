# 뱀 ( 정답 )
# 보드에서 사과만 1 나머지 0
# 방향 전환과 뱀 상태 각각 디큐에 저장



import sys
from collections import deque
input = sys.stdin.readline

# 방향 전환 함수
def change_now(now,w):
    if now == 0 and w=="L":
        return 2
    elif now == 0 and w=="D":
        return 3
    elif now == 1 and w=="L":
        return 3
    elif now == 1 and w=="D":
        return 2
    elif now == 2 and w=="L":
        return 1
    elif now == 2 and w=="D":
        return 0
    elif now == 3 and w=="L":
        return 0
    else: #now == 3 and w=="D":
        return 1



n = int(input())
k = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(k):
    x,y = tuple(map(int,input().split()))
    arr[x-1][y-1] = 1

# for i in range(n):
#     print(arr[i])

l = int(input())
turn = deque()
for i in range(l):
    temp1, temp2 = map(str,input().split())
    turn.append((int(temp1),temp2))
# print(turn)

queue = deque()

# 상 하 좌 우
xy = [[-1,0],[1,0],[0,-1],[0,1]]
# 현재 방향
now = 3
queue.append((0,0))
time = 0
while True:
    # print(queue)
    time += 1
    x,y = queue[0]
    x = x + xy[now][0]
    y = y + xy[now][1]

    # 자신을 만난경우
    if (x,y) in queue:
        print(time)
        break
    # 벽에 닿은 경우
    if x < 0 or x >= n or y < 0 or y >= n:
        print(time)
        break
    
    # 사과를 만난경우 꼬리 줄이지 않음
    if arr[x][y] == 1:
        queue.appendleft((x,y))
        arr[x][y] = 0
    # 사과가 아닌경우 꼬리 줄임
    else :
        queue.appendleft((x,y))
        queue.pop()

    # 방향전환 입력 시간순서이므로 앞에서부터
    if len(turn) != 0:
        t,w = turn[0]
        if time == t:
            now = change_now(now,w)
            turn.popleft()

