# 텀 프로젝트 ( 79% 시간초과 )

import sys
from collections import deque

sys.setrecursionlimit(111111)

def find(x):
    # print("find(x)",x)                                                      #

    # 본인이 본인 선택
    if x == s[x]:
        visited[x] = True
    
    # 이미 팀이 있는사람 선택
    elif visited[s[x]] == True:
        queue.append(x)

    # 되돌아와 팀 생성
    elif len(queue) != 0 and queue[0] == x:
        for i in range(len(queue)):
            visited[queue[i]] = True
        queue.clear()


    # 자신이 큐의 첫번째가 아닌 자리에 있으면 그자리부터 끝까지가 팀
    elif len(queue) != 0 and (x in queue) and (queue[0] != x):
        temp=0
        qlen = len(queue)
        for i in range(qlen):
            if queue[i] == x:
                temp = i
                break
        for i in range(qlen-1,temp-1,-1):
            visited[queue[i]] = True
            queue.pop()
        # print(visited)                                                      #
        # print(queue)                                                        #
    
    # 그 외
    else:
        queue.append(x)
        # print(queue)                                                        #
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


    # 그룹 못만든 학생들
    failgroup = []
    
    
    for i in range(1,n+1):
        # print("i:",i)                                                       #
        if visited[i] == True:
            continue
        else:
            queue = deque()
            find(i)

            # 그룹 못만든 학생 추가
            for j in queue:
                if visited[j] == False:
                    failgroup.append(j)
                    visited[j] = True
            # print("failgroup",failgroup)                                        #


    print(len(failgroup))

