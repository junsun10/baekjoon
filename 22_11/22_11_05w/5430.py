# AC ( 정답 )
# 알고리즘 : 구현
# 배열 뒤집기를 매번 하면 시간초과가 나기 때문에
# 마지막 상태를 기준으로 뒤집는다
# 따라서 D명령어를 왼쪽에서 뺄지 오른쪽에서 뺄지 따로 확인해야함

t = int(input())

for _ in range(t):
    p = input()  # 명령어
    n = int(input())  # 배열 길이
    temp = input()  # 배열
    if len(temp) == 2:
        arr = []
    else:
        temp = temp[1:-1]
        arr = list(map(int, temp.split(",")))
    arrLength = len(arr)

    reverse = False  # 배열 상태
    countR = 0
    countLeftD = 0
    countRightD = 0
    for i in p:
        if i == "R":
            countR += 1
            reverse = not reverse
        else:
            if reverse:
                countRightD += 1
            else:
                countLeftD += 1

    # 배열 길이보다 D 명령어 개수가 클때
    if countLeftD + countRightD > arrLength:
        print("error")
    else:
        if countLeftD != 0 and countRightD != 0:
            arr = arr[countLeftD:-countRightD]
        elif countLeftD == 0 and countRightD != 0:
            arr = arr[:-countRightD]
        elif countLeftD != 0 and countRightD == 0:
            arr = arr[countLeftD:]

        # 뒤집힌 상태면 한번 뒤집음
        if reverse:
            arr.reverse()

        # 조건에 맞게 출력
        print("[", end="")
        for i in range(len(arr)):
            print(arr[i], end="")
            if i < len(arr)-1:
                print(",", end="")
        print("]")
