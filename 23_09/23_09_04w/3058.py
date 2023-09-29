# 짝수를 찾아라 ( 정답 )

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    temp = []
    for i in arr:
        if i % 2 == 0:
            temp.append(i)

    print(sum(temp), min(temp))
