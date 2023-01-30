# 킹, 퀸, 룩, 비숍, 나이트, 폰 ( 정답 )
# 알고리즘 : 수학, 구현

chess = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))

for i in range(6):
    print(chess[i]-arr[i], end=" ")
print()
