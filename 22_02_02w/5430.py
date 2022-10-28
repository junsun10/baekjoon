# AC ( 시간초과 )
# 큐사용


import sys
from collections import deque


# 테스트 케이스 개수만큼 반복
t = int(sys.stdin.readline())
for _ in range(t):

    # 에러 확인 변수
    error = False

    # 함수 입력
    p = list(map(str,sys.stdin.readline().strip()))
    # print(p)

    # 배열 길이 입력
    n = int(sys.stdin.readline())
    # print(n)

    # 배열 입력
    temp = sys.stdin.readline()
    temp = temp[1:-2]       # [,],\n 제거
    if len(temp) == 0:
        arr = []
    else:
        arr = list(map(int,temp.split(",")))

    # 큐에 저장
    queue = deque()
    for i in range(n):
        queue.append(arr[i])
    
    # 함수 실행
    for i in range(len(p)):

        # 뒤집기
        if p[i] == 'R':
            temp = deque()
            for j in range(len(queue)):
                temp.append(queue.pop())
                # print(temp)
            queue = temp    
            # print(queue)

        # 왼쪽 버리기
        else:
            if len(queue) == 0:
                print("error")
                error = True
                break
            else:
                queue.popleft()
                # print(queue)

    if error:
        continue
    
    # 형식에 맞게 출력
    if len(queue) == 0:
        print("[]")
    elif len(queue) == 1:
        print("[",end="")
        print(queue[0],end="")
        print("]")
    else:
        print("[",end="")
        for i in range(len(queue)-1):
            print(queue[i],end = "")
            print(",",end="")
        print(queue[len(queue)-1],end="")
        print("]")

