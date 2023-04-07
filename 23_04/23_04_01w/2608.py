# 로마 숫자 ( 정답 )
# 알고리즘 : 구현

# IV:4, IX:9, XL:40, XC:90, CD:400, CM:900
r2i = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
a = list(input())
b = list(input())


def get_num(x):
    value = 0
    check = 0
    for i, v in enumerate(x):
        if v == "I" and i < len(x)-1 and x[i+1] == "V":
            value += 4
            check = 1
        elif v == "I" and i < len(x)-1 and x[i+1] == "X":
            value += 9
            check = 1
        elif v == "X" and i < len(x)-1 and x[i+1] == "L":
            value += 40
            check = 1
        elif v == "X" and i < len(x)-1 and x[i+1] == "C":
            value += 90
            check = 1
        elif v == "C" and i < len(x)-1 and x[i+1] == "D":
            value += 400
            check = 1
        elif v == "C" and i < len(x)-1 and x[i+1] == "M":
            value += 900
            check = 1
        else:
            if check == 1:
                check = 0
                continue
            else:
                value += r2i[v]
    return value


def get_rom(x):
    s = ""

    s += "M"*(x//1000)
    x = x % 1000

    if x >= 900:
        s += "CM"
        x -= 900
    if x >= 500:
        s += "D"
        x -= 500

    if x >= 400:
        s += "CD"
        x -= 400

    s += "C"*(x//100)
    x = x % 100

    if x >= 90:
        s += "XC"
        x -= 90

    if x >= 50:
        s += "L"
        x -= 50

    if x >= 40:
        s += "XL"
        x -= 40

    s += "X"*(x//10)
    x = x % 10

    if x >= 9:
        s += "IX"
        x -= 9

    if x >= 5:
        s += "V"
        x -= 5

    if x >= 4:
        s += "IV"
        x -= 4

    s += "I"*x

    return s


a_v = get_num(a)
b_v = get_num(b)
print(a_v+b_v)
print(get_rom(a_v+b_v))
