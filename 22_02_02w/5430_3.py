# AC ( 정답 ) 
# R과 D를 매번 실행했더니 시간초과가 뜸
# R의 개수를 세서 마지막에 짝수면 유지, 홀수면 뒤집음
# D는 뒤집힌 상태에서 빼는지 원래 상태에서 빼는지 따로 세서 앞뒤를 한번에 제거


import sys

# 테스트 케이스 개수만큼 반복
t = int(sys.stdin.readline())
for _ in range(t):

    # 함수 입력
    p = list(map(str,sys.stdin.readline().strip()))
    # print(p)

    # R 개수와 D 위치 계산
    # R의 개수가 짝수면 앞에서 제거
    # R의 개수가 홀수면 뒤에서 제거
    countR=0
    front=0
    end=0
    for i in range(len(p)):
        if p[i]=="R":
            countR+=1
        else:
            if countR%2==0:
                front+=1
            else:
                end+=1


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

    
    # 함수 실행

    # front, end 빼주기
    if front + end > n:
        print("error")
        continue
    elif end == 0:
        arr = arr[front:]
    else:
        arr = arr[front:-end]

    # 홀수면 뒤집기
    if countR % 2 == 1:
        temp = []
        for j in range(len(arr)-1,-1,-1):
            temp.append(arr[j])
            # print(temp)
        arr = temp    
       

    # 형식에 맞게 출력
    # 처음에 print(arr)로 했더니 틀림
    if len(arr) == 0:
        print("[]")
    elif len(arr) == 1:
        print("[",end="")
        print(arr[0],end="")
        print("]")
    else:
        print("[",end="")
        for i in range(len(arr)-1):
            print(arr[i],end = "")
            print(",",end="")
        print(arr[len(arr)-1],end="")
        print("]")
