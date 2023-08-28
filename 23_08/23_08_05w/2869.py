# 달팽이는 올라가고 싶다 ( 정답 )
# 알고리즘: 수학
# 낮에 올라가서 끝나는 경우 고려해야 함
# 먼저 v에서 a만큼 빼고 계산

a, b, v = map(int, input().split())

v -= a

day = 1 + v//(a-b)

if v % (a-b) > 0:
    day += 1

print(day)
