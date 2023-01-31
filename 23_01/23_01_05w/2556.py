# 최댓값 ( 정답 )
# 알고리즘 : 구현

arr = [list(map(int, input().split())) for _ in range(9)]
max_val = -1
max_index = [-1, -1]

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            max_index = [i+1, j+1]

print(max_val)
print(max_index[0], max_index[1])
