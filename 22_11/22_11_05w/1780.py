# 종이의 개수 ( 정답 )
# 알고리즘 : 재귀, 분할정복
# 조건에 따라 재귀 함수 호출

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0, 0]


# 배열 자르는 함수
def cut(x, y, k):
    temp = check(x, y, k)
    if temp == -1:
        answer[0] += 1
    elif temp == 0:
        answer[1] += 1
    elif temp == 1:
        answer[2] += 1
    else:
        cut(x, y, k//3)
        cut(x, y+(k//3), k//3)
        cut(x, y+2*(k//3), k//3)
        cut(x+(k//3), y, k//3)
        cut(x+(k//3), y+(k//3), k//3)
        cut(x+(k//3), y+2*(k//3), k//3)
        cut(x+2*(k//3), y, k//3)
        cut(x+2*(k//3), y+(k//3), k//3)
        cut(x+2*(k//3), y+2*(k//3), k//3)


# 범위내 배열이 어떻게 구성돼있는지 확인
def check(x, y, k):
    temp = [0, 0, 0]
    for i in range(x, x+k):
        for j in range(y, y+k):
            if arr[i][j] == -1:
                temp[0] += 1
            elif arr[i][j] == 0:
                temp[1] += 1
            else:
                temp[2] += 1
    if temp[0] == k**2:
        return -1
    elif temp[1] == k**2:
        return 0
    elif temp[2] == k**2:
        return 1
    else:
        return 2


cut(0, 0, n)
for a in answer:
    print(a)
