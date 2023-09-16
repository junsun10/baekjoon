# 행렬 ( 정답 )
# 알고리즘: 그리디
# (0,0)부터 시작해서 정답 행렬과 다르면 변환

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
answer = [list(input()) for _ in range(n)]
count = 0


def change(arr, x, y):
    for i in range(3):
        for j in range(3):
            if arr[x+i][y+j] == "0":
                arr[x+i][y+j] = "1"
            else:
                arr[x+i][y+j] = "0"
    return arr


for i in range(n-2):
    for j in range(m-2):
        # print(i, j)
        if arr[i][j] != answer[i][j]:
            arr = change(arr, i, j)
            count += 1

        # for k in arr:
        #     print(k)
if arr == answer:
    print(count)
else:
    print(-1)
