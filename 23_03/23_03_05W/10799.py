# 쇠막대기
# 알고리즘 : 스택
# 파이프가 열릴 때 현재까지 생긴 레이저 수를 저장
# 파이프가 닫힐 때 현재까지 생긴 레이저 수에서
# 열릴 때 레이저 수를 뺀 뒤 1을 더함

x = input()

razer = 0
pipe_list = []
answer = 0

for index, value in enumerate(x):
    if value == "(":
        pipe_list.append(razer)
    else:
        if x[index-1] == "(":
            razer += 1
            pipe_list.pop()
        else:
            count = pipe_list.pop()
            answer += razer - count + 1

print(answer)
