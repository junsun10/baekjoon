# 색종이 만들기 ( 정답 )
# 알고리즘 : 재귀, 분할정복
# 조건에 따라 재귀 함수 호출

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0


def paper(x, y, l):
    global white, blue
    if l == 1:
        for i in range(x, x+l):
            for j in range(y, y+l):
                if arr[i][j] == 0:
                    white += 1
                else:
                    blue += 1
    else:
        tempWhite = 0
        tempBlue = 0
        for i in range(x, x+l):
            for j in range(y, y+l):
                if arr[i][j] == 0:
                    tempWhite += 1
                else:
                    tempBlue += 1
        if tempWhite == l**2:
            white += 1
        elif tempBlue == l**2:
            blue += 1
        else:
            paper(x, y, l//2)
            paper(x, y+l//2, l//2)
            paper(x+l//2, y, l//2)
            paper(x+l//2, y+l//2, l//2)


paper(0, 0, n)

print(white)
print(blue)
