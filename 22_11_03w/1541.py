# 잃어버린 괄호 ( 정답 )
# 알고리즘 : 완전 탐색
# "-"뒤의 "+"끼리 모두 더한 후 뺀다

inputString = input()
answer = 0
numArr = []
plusMinusArr = []
temp = ""
for i in range(len(inputString)):
    if inputString[i] == "-" or inputString[i] == "+":
        numArr.append(int(temp))
        temp = ""
        plusMinusArr.append(inputString[i])
    else:
        temp += inputString[i]
numArr.append(int(temp))

if "-" not in plusMinusArr:
    print(sum(numArr))
else:
    tempMinus = 0
    tempPlus = 0
    status = False
    for i in range(len(plusMinusArr)):
        if plusMinusArr[i] == "-":
            status = True
            tempMinus += numArr[i+1]
        else:
            if status:
                tempMinus += numArr[i+1]
            else:
                tempPlus += numArr[i+1]
    print(numArr[0]-tempMinus+tempPlus)
