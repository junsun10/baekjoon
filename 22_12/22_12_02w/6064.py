# 카잉 달력 ( 정답 )
# 알고리즘 : 수학
# 최소공배수까지 계산하면 시간초과
# 규칙을 찾아서 해결

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())

    find = False
    if m < n:
        for i in range(n):
            # 규칙
            if ((m * i + x) - y) % n == 0:
                print(m*i+x)
                find = True
                break
    else:
        for i in range(m):
            # 규칙
            if ((n * i + y) - x) % m == 0:
                print((n*i+y))
                find = True
                break
    if not find:
        print(-1)
