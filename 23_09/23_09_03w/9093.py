# 단어 뒤집기 ( 정답 )
# 알고리즘: 문자열

for _ in range(int(input())):
    arr = list(map(str, input().split()))

    for i in arr:
        for j in range(len(i)):
            print(i[-j-1], end="")
        print(" ", end="")
    print()
