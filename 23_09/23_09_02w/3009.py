# 네 번째 점 ( 정답 )
# 알고리즘: 구현

x = []
y = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()
answer = []

if x[0] == x[1]:
    answer.append(x[2])
else:
    answer.append(x[0])
if y[0] == y[1]:
    answer.append(y[2])
else:
    answer.append(y[0])

print(answer[0], answer[1])
