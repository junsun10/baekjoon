# 평균은 넘겠지 ( 정답 )
# 알고리즘: 수학

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:]) / arr[0]
    count = 0
    for i in range(1, arr[0]+1):
        if arr[i] > avg:
            count += 1
    answer = count / arr[0] * 100
    answer = round(answer, 3)
    print(f"{answer:.3f}%")
