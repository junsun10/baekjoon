# 집합 ( 정답 )
# 알고리즘 : 집합
# pypy3 메모리 초과 python3 정답

import sys

s = set()

for _ in range(int(sys.stdin.readline())):
    inputStr = list(sys.stdin.readline().split())

    if len(inputStr) == 1:
        if inputStr[0] == "all":
            s.update([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                      12, 13, 14, 15, 16, 17, 18, 19, 20])
        else:
            s = set()

    else:
        instr = inputStr[0]
        num = int(inputStr[1])

        if instr == "add":
            s.add(num)
        elif instr == "remove":
            s.discard(num)
        elif instr == "check":
            if num in s:
                print(1)
            else:
                print(0)
        elif instr == "toggle":
            if num in s:
                s.remove(num)
            else:
                s.add(num)
