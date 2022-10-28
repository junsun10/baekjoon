# 테트로미노 ( 시간초과 )

from asyncio import queues
import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
xy = [(-1,0),(0,1),(1,0),(0,-1)]

answer = []
answer_val = []


for i in range(n):
    for j in range(m):
        queue = deque()
        queue.append([(i,j)])
        # print(queue[0])

        # i,j시작 경우의수 만들기
        while len(queue[0]) < 4:
            if len(queue[0])==1:
                for k in range(4):
                    temp = queue[0][:]
                    new_x = queue[0][-1][0]+xy[k][0]
                    new_y = queue[0][-1][1]+xy[k][1]
                    if 0<=new_x<=n-1 and 0<=new_y<=m-1 and (new_x,new_y) not in temp:
                        temp.append((new_x,new_y))

                        if temp not in queue:
                            queue.append(temp)
                            
                    if k == 3:
                        queue.popleft()
            else:
                for l in range(1,len(queue[0])):

                    for k in range(4):
                        temp = queue[0][:]
                        new_x = queue[0][-l][0]+xy[k][0]
                        new_y = queue[0][-l][1]+xy[k][1]
                        if 0<=new_x<=n-1 and 0<=new_y<=m-1 and (new_x,new_y) not in temp:
                            temp.append((new_x,new_y))

                            # if temp not in queue: aaa
                            if temp not in queue and temp not in answer:
                                queue.append(temp)
                                
                    if l == len(queue[0])-1:
                        queue.popleft()
                    # print(queue)
        # print(queue)

        # 추가한부분
        for k in queue:
            if k not in answer:
                answer.append(k)

        max_val = 0
        for k in range(len(queue)):
            temp = 0
            for l in range(4):
                x = queue[k][l][0]
                y = queue[k][l][1]
                temp += arr[x][y]
            if temp > max_val:
                max_val = temp
        # print(max_val)
        answer_val.append(max_val)
print(max(answer_val))