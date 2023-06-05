# 하노이 탑 이동 순서 ( 정답 )
# 알고리즘 : 재귀

n = int(input())
count = 0
answer = []


# a, b, c : 시작, 보조, 목표
def f(a, b, c, num):
    global count
    if num > 0:
        count += 1
        f(a, c, b, num-1)
        answer.append(f"{a} {c}")
        f(b, a, c, num-1)


f(1, 2, 3, n)
print(count)
for i in answer:
    print(i)
