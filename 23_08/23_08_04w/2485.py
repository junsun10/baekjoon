# 가로수 (정답)
# 알고리즘: 수학
# 가로수들 사이의 간격과 가장 짧은 간격을 저장
# 가장 짧은 간격부터 시작해서 모든 간격과 나누어 떨엉지는 최대 간격 탐색
# 가로수 사이의 간격의 최대공약수

n = int(input())
trees = []
between = []
min_length = 10**9

for i in range(n):
    now = int(input())
    if i == 0:
        trees.append(now)
    else:
        trees.append(now)
        length = now - trees[i-1]
        between.append(length)
        min_length = min(length, min_length)

# 모든 간격과 나누어 떨어지는 최대 간격 탐색
end = False
for i in range(min_length, 0, -1):
    count = 0
    for index, length in enumerate(between):
        # 간격이 나누어 떨어지지 않으면 탈출
        if length % i != 0:
            break
        count += length//i - 1
        # 마지막 간격까지 나누어 떨어지면 종료
        if index == len(between)-1:
            end = True
    if end:
        break

print(count)
