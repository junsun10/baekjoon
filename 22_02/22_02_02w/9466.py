# 텀 프로젝트 ( 틀림 )

import sys
from collections import deque


def find(x):
    if (x in queue) and queue[0] != x:
        queue.clear()
        return
    queue.append(x)
    # print("x, queue :",x,queue)
    # 마지막이 처음으로 되돌아와서 팀 생성
    if len(queue) != 1 and queue[0] == queue[-1]:
        for i in queue:
            visited[i] = True
        queue.clear()

    # 자기자신
    elif x == s[x]:
        visited[x] = True
        queue.pop()
    else:
        if visited[s[x]] == False:
            find(s[x])



# T 입력
t = int(sys.stdin.readline())
for _ in range(t):

    # 학생수, 선택한 학생 배열 입력
    n = int(sys.stdin.readline())
    s = list(map(int,sys.stdin.readline().split()))
    s = [0] + s
    

    # 그룹 만들어지면 True
    visited=[False for _ in range(n+1)]

    # 그룹 못만든 학생 True
    fail = [False for _ in range(n+1)]

    # 그룹 못만든 학생들
    failgroup = []
    
    
    for i in range(1,n+1):
        # print("i:",i)
        if visited[i] == True:
            continue
        queue = deque()
        find(i)

        # 그룹 못만든 학생 추가
        for j in queue:
            if fail[j] == False:
                failgroup.append(j)
                fail[j] = True
        # print(failgroup)


    print(len(failgroup))


# 반례
# 2 3 5 5 4


        
