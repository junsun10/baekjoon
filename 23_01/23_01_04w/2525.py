# 오븐 시계 ( 정답 )
# 알고리즘 : 수학

nh, nm = map(int, input().split())
time = int(input())

h = time//60
m = time % 60

nm += m
if nm >= 60:
    nh += 1
    nm = nm % 60

nh += h
nh = nh % 24

print(nh, nm)
