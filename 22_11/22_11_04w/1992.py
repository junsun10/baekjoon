# 쿼드트리 ( 정답 )
# 알고리즘 : 분할정복, 재귀
# 네가지 경우의 수를 재귀로 호출

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]


def check(n, x, y):
    temp = countNum(n, x, y)
    if temp == 0:
        print(0, end="")
    elif temp == 1:
        print(1, end="")
    else:
        if n//2 > 1:
            print("(", end="")
            check(n//2, x, y)
            check(n//2, x, y+n//2)
            check(n//2, x+n//2, y)
            check(n//2, x+n//2, y+n//2)
            print(")", end="")
        else:
            print("(", end="")
            for i in range(x, x+n):
                for j in range(y, y+n):
                    print(arr[i][j], end="")
            print(")", end="")


def countNum(n, x, y):
    count0 = 0
    count1 = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] == 0:
                count0 += 1
            else:
                count1 += 1
    if count0 == n**2:
        return 0
    elif count1 == n**2:
        return 1
    else:
        return -1


check(n, 0, 0)
print()
