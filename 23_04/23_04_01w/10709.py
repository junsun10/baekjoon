# 기상캐스터 ( 정답 )
# 알고리즘 : 구현

H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]

for i in range(H):
    last = -1
    for j in range(W):
        if arr[i][j] == "c":
            print(0, end=" ")
            last = j
        else:
            if last == -1:
                print(-1, end=" ")
            else:
                print(j-last, end=" ")
    print()
