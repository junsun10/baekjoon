# 평균 ( 정답 )
# 알고리즘 : 수학

n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)

for i in range(n):
    arr[i] = arr[i]/max_val*100

print(sum(arr)/n)
