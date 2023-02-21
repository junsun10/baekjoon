# 참외밭 ( 정답 )
# 알고리즘 : 구현, 기하학

from collections import deque
k = int(input())

e, w, s, n = [], [], [], []
list = deque()

for _ in range(6):
    t, l = map(int, input().split())
    list.append([t, l])
    if t == 1:
        e.append(l)
    elif t == 2:
        w.append(l)
    elif t == 3:
        s.append(l)
    else:
        n.append(l)

width = sum(e)
height = sum(s)
big = sum(e)*sum(s)
small = 0

while True:
    if list[0][1] != height:
        list.rotate(-1)
    else:
        break
if list[1][1] == width:
    small = list[3][1]*list[4][1]
else:
    small = list[2][1]*list[3][1]


print((big-small)*k)
