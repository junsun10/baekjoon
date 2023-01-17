# 괄호 ( 정답 )
# 알고리즘 : 자료구조, 문자열, 스택

t = int(input())

for _ in range(t):
    arr = []
    answer = True
    s = input()
    for i in s:
        if i == "(":
            arr.append("(")
        else:
            if len(arr) > 0 and arr[-1] == "(":
                arr.pop()
            else:
                answer = False
                break
    if len(arr) == 0 and answer:
        print("YES")
    else:
        print("NO")
