# 괄호의 값 ( 정답 )
# 알고리즘 : 스택, 구현
# 올바르지 못한 괄호 처리 중요

from collections import deque

arr = input()

dq = deque()
cal = deque()
count = []
check = True

for i in range(len(arr)):
    if arr[i] == "(":
        dq.append("(")
        count.append(0)

    elif arr[i] == "[":
        dq.append("[")
        count.append(1)

    elif arr[i] == ")":
        if len(count) == 0 or count[-1] != 0:
            check = False
            break
        else:
            temp = 0
            # ( 2 9 ) 같은 2와 9를 더한 뒤 곱하기 해야 하는 경우 확인
            while True:
                if len(dq) > 0:
                    if type(dq[-1]) == int:
                        temp += dq.pop()
                    else:
                        k = dq.pop()
                        # ()로 2인 경우
                        if temp == 0:
                            dq.append(2)
                        # 곱하기 2인 경우
                        else:
                            dq.append(temp*2)
                        count.pop()
                        break

    else:
        if len(count) == 0 or count[-1] != 1:
            check = False
            break
        else:
            temp = 0
            while True:
                if len(dq) > 0:
                    if type(dq[-1]) == int:
                        temp += dq.pop()
                    else:
                        k = dq.pop()
                        if temp == 0:
                            dq.append(3)
                        else:
                            dq.append(temp*3)
                        count.pop()
                        break

if len(count) == 0 and check:
    print(sum(dq))
else:
    print(0)
