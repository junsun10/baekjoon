# 너의 평점은 ( 정답 )
# 알고리즘: 수학

answer = 0
t = 0

for _ in range(20):
    a, b, c = map(str, input().split())

    if c != "P":
        t += float(b)

    temp = 0

    if c == "A+":
        temp = 4.5
    elif c == "A0":
        temp = 4.0
    elif c == "B+":
        temp = 3.5
    elif c == "B0":
        temp = 3.0
    elif c == "C+":
        temp = 2.5
    elif c == "C0":
        temp = 2.0
    elif c == "D+":
        temp = 1.5
    elif c == "D0":
        temp = 1.0
    else:
        temp = 0

    answer += temp * float(b)

print(f"{answer/t:.6f}")
