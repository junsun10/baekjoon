# AC ( 시간초과 )
# 배열 사용

import sys


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


    count=0
    # 함수 실행
    for i in range(len(p)):
        # print(arr)
        # 뒤집기
        if p[i] == 'R':
            count+=1
            # 함수의 마지막이 R 일때
            if i == len(p)-1:
                # 짝수면 유지
                if count%2==0:
                    continue
                # 홀수면 뒤집기
                else:
                    temp = []
                    for j in range(len(arr)-1,-1,-1):
                        temp.append(arr[j])
                        # print(temp)
                    arr = temp    
                    # print(arr)
                    count=0

            # 다음이 D 일때
            elif p[i+1] == "D":
                # 짝수면 유지
                if count%2==0:
                    continue
                # 홀수면 뒤집기
                else:
                    temp = []
                    for j in range(len(arr)-1,-1,-1):
                        temp.append(arr[j])
                        # print(temp)
                    arr = temp    
                    # print(arr)
                    count=0

            # 다음이 R 일때
            else:
                continue

        # 왼쪽 버리기
        else:
            count=0
            if len(arr) == 0:
                print("error")
                error = True
                break
            else:
                arr = arr[1:]
                # print(arr)

        

    if error:
        continue

    print(arr)
