# 개발자 지망생 구름이의 취업 뽀개기 ( 정답 )
# 알고리즘: 구현
# 시간이 짧은 문제부터 선택

n = int(input())
n_solve = list(map(int, input().split()))
p = [[] for _ in range(6)]

for _ in range(n):
    l, t = map(int, input().split())

    p[l].append(t)

for i in range(6):
    p[i].sort()

time = 0
for i in range(5):
    count = n_solve[i]
    for j in range(count):
        if j > 0:
            time += p[i+1][j] - p[i+1][j-1]
        time += p[i+1][j]
    time += 60

print(time-60)
