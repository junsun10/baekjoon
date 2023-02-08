# 최소공배수 ( 정답 )
# 알고리즘 : 수학

import sys

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        a, b = b, a
    temp = 1
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            temp = i
    print(temp*(a//temp)*(b//temp))
