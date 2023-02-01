# 다리 놓기 ( 정답 )
# 알고리즘 : 수학
# 조합 계산하는 문제

for _ in range(int(input())):
    n, m = map(int, input().split())
    if n == 0 or m == 0:
        print(0)
        continue
    answer = 1
    for i in range(n):
        answer *= m-i
    for i in range(1, n+1):
        answer = answer//i
    print(answer)
