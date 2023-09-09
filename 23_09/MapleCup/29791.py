# 에르다 노바와 오리진 스킬 ( 정답 )
# 알고리즘: 정렬

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

time_a = 0
time_b = 0
count_a = 0
count_b = 0


for i in range(n):
    temp = a[i]
    if temp >= time_a:
        count_a += 1
        time_a = temp + 100

for i in range(m):
    temp = b[i]
    if temp >= time_b:
        count_b += 1
        time_b = temp + 360

print(count_a, count_b)
