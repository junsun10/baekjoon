# 연속합 ( 정답[이현풀이] )
# 알고리즘 : dp

n = int(input())
arr = list(map(int, input().split()))
arr_sum = [-1000000000]*(n+1)

for i in range(1, n+1):
    arr_sum[i] = max(arr[i-1], arr_sum[i-1]+arr[i-1])

print(max(arr_sum))
