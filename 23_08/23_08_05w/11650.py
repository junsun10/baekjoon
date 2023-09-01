# 좌표 정렬하기 ( 정답 )
# 알고리즘: 정렬


n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))

arr.sort(key=lambda x: (x[0], x[1]))

# for i in range(n-1):
#     for j in range(i+1, n):
#         if arr[i][0] > arr[j][0]:
#             arr[i], arr[j] = arr[j], arr[i]
#         elif arr[i][0] == arr[j][0] and arr[i][1] > arr[j][1]:
#             arr[i], arr[j] = arr[j], arr[i]

for i in arr:
    print(*i)
