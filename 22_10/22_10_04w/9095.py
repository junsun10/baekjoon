# 1, 2, 3 더하기
# 알고리즘 : 재귀
# 가능한 경우의 수 재귀

t = int(input())
arr = [int(input()) for _ in range(t)]


def f(x):
    global answer

    if x == 0:
        answer += 1
        return 0

    if x >= 3:
        f(x-1)
        f(x-2)
        f(x-3)
    elif x == 2:
        f(x-1)
        f(x-2)
    else:
        f(x-1)


for i in arr:
    answer = 0
    f(i)
    print(answer)
