# 나누기 ( 정답 )
# 알고리즘 : 완전탐색

n = int(input())
f = int(input())

temp = n - n % 100

answer = 0
for i in range(temp, temp+100):
    if i % f == 0:
        answer = i
        break

answer -= temp
if answer < 10:
    print("0"+str(answer))
else:
    print(str(answer))
