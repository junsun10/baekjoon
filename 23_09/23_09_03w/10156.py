# 과자 ( 정답 )

k, n, m = map(int, input().split())

answer = m - k * n

if answer < 0:
    print(-answer)
else:
    print(0)
