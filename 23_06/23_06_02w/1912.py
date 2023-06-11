# 연속합 ( 정답 )
# 알고리즘 : dp
# 누적합을 구한 뒤
# 전체 돌면서 누적합 최대 선택
# 단 이전까지 최소 누적합이 음수인 경우에는 누적합에서 빼서 최대값 갱신

n = int(input())
arr = list(map(int, input().split()))
arr_sum = [arr[0]]
for i in range(1, n):
    arr_sum.append(arr_sum[i-1] + arr[i])

min_val = 1000000000
answer = -1000000000
for i in range(n):

    if min_val < 0:
        if answer < arr_sum[i] - min_val:
            answer = arr_sum[i] - min_val

    if arr_sum[i] < min_val:
        min_val = arr_sum[i]

    if arr_sum[i] > answer:
        answer = arr_sum[i]

print(answer)
