# 셀프 넘버 ( 정답 )
# 알고리즘 : 구현, 완전 탐색

check = [False for _ in range(10001)]


def f(n):
    ans = n
    temp = n
    while temp > 0:
        ans += temp % 10
        temp = temp // 10

    return ans


for i in range(1, 10001):
    temp = f(i)
    if temp <= 10000:
        check[temp] = True

for i in range(1, 10001):
    if not check[i]:
        print(i)
