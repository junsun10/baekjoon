# 게임 ( 정답 )
# 알고리즘: 이분탐색

x, y = map(int, input().split())
z = (100*y)//x

if z >= 99:
    print(-1)
else:
    start = 1
    end = 2**32-1
    save = 1
    while start <= end:
        point = (start+end)//2
        if (100*(y+point))//(x+point) >= z + 1:
            save = point
            end = point - 1
        else:
            start = point + 1

    print(save)
