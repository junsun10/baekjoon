# 직각삼각형 ( 정답 )
# 알고리즘 : 기하학
# 피타고라스 정리

while True:
    arr = list(map(int, input().split()))

    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        break

    arr.sort()
    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        print("right")
    else:
        print("wrong")
