# 텀 프로젝트 ( 79% 런타임에러 )

import sys
from collections import deque


def find(x):

    # 자신이 큐의 첫번째가 아닌 자리에 있으면 팀 생성 불가
    if (x in queue) and queue[0] != x:
        temp=0
        qlen = len(queue)
        for i in range(len(queue)):
            if queue[i] == x:
                temp = i
                break
        for i in range(qlen-temp):
            queue.pop()
        return

    queue.append(x)
    # print("x, queue :",x,queue)

    # 마지막이 처음을 선택해 팀 생성 
    if len(queue) != 1 and queue[0] == queue[-1]:
        for i in queue:
            visited[i] = True
        queue.clear()
    
    # 본인이 본인 선택
    elif x == s[x]:
        visited[x] = True
        queue.pop()
    
    # 그 외
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
    

    # 방문 여부
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


