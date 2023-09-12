# 평균 점수 ( 정답 )
# 알고리즘: 수학

arr = [int(input()) for _ in range(5)]
for i in range(5):
    if arr[i] < 40:
        arr[i] = 40

print(sum(arr)//5)
