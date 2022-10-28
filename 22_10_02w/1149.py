# RGB 거리 ( 정답 )
# 알고리즘: DP
# 각 자리별 이전 까지의 최솟값을 새로운 배열에 저장하면서 진행

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
new_arr = [[0, 0, 0] for _ in range(n)]
new_arr[0][0], new_arr[0][1], new_arr[0][2] = arr[0][0], arr[0][1], arr[0][2]

for i in range(1, n):
    new_arr[i][0] = min(new_arr[i-1][1], new_arr[i-1][2]) + arr[i][0]
    new_arr[i][1] = min(new_arr[i-1][0], new_arr[i-1][2]) + arr[i][1]
    new_arr[i][2] = min(new_arr[i-1][0], new_arr[i-1][1]) + arr[i][2]

print(min(new_arr[n-1]))
