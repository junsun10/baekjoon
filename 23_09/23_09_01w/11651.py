# 좌표 정렬하기 ( 정답 )
# 알고리즘: 정렬

arr = []
for i in range(int(input())):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: [x[1], x[0]])

for i in arr:
    print(*i)
