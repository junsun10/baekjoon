# 음계 ( 정답 )
# 알고리즘 : 구현

n = list(map(int, input().split()))
mixed = False

if n[0] == 1:
    for i in range(1, len(n)):
        if n[i] != n[i-1] + 1:
            mixed = True
            break
    if not mixed:
        print("ascending")
    else:
        print("mixed")
elif n[0] == 8:
    for i in range(1, len(n)):
        if n[i] != n[i-1]-1:
            mixed = True
            break
    if not mixed:
        print("descending")
    else:
        print("mixed")
else:
    print("mixed")
