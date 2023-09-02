# 탭 UI ( 정답 )
# 알고리즘: 누적합
# 조건문을 통해 양쪽 끝 예외처리
# 누적합으로 계산 시간 단축

import sys

n = int(sys.stdin.readline())
tab = []
dp = []
for i in range(n):
    t = int(sys.stdin.readline())
    tab.append(t)
    if i > 0:
        dp.append(dp[i-1]+t)
    else:
        dp.append(t)


l = int(sys.stdin.readline())
q = int(sys.stdin.readline())

total_length = dp[-1]

for _ in range(q):
    num = int(sys.stdin.readline())
    num -= 1

    if num == 0:
        x = tab[num]/2
    else:
        x = dp[num-1] + tab[num]/2

    if x > l/2:
        if x + l/2 > total_length:
            if total_length - l < 0:
                print(f"{0:.2f}")
            else:
                print(f"{total_length-l:.2f}")
        else:
            print(f"{x-l/2:.2f}")
    else:
        print(f"{0:.2f}")
