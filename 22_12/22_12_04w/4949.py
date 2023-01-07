# 균형잡힌 세상 ( 정답 )
# 알고리즘 : 스택
# 열린 괄호 개수 스택에 저장


while True:
    line = input()
    small = []
    big = []
    count = 1
    good = True
    if line == ".":
        break
    else:
        for i in line:
            if i == "(":
                small.append(count)
                count += 1
            elif i == "[":
                big.append(count)
                count += 1
            elif i == ")":
                if count-1 in small:
                    small.pop()
                    count -= 1
                else:
                    good = False
                    break
            elif i == "]":
                if count-1 in big:
                    big.pop()
                    count -= 1
                else:
                    good = False
                    break
            else:
                continue
        if len(small) != 0 or len(big) != 0:
            good = False

        if not good:
            print("no")
        else:
            print("yes")
