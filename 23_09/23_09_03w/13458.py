# 시험감독 ( 정답 )
# 알고리즘: 수학

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0

for i in arr:
    temp = i - b
    answer += 1
    if temp <= 0:
        continue
    else:
        answer += temp // c
        if temp % c != 0:
            answer += 1
print(answer)
