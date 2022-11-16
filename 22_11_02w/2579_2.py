# 계단 오르기 ( 시간 초과 )

numOfStairs = int(input())
stairsArr = [int(input()) for _ in range(numOfStairs)]
answer = 0


def pick(now):

    if len(now) == numOfStairs - 1:
        if now[-2] == 0 and now[-1] == 1:
            temp = now[:]
            temp.append(1)
            findAnswer(temp)
            return
        elif now[-1] == 0:
            temp = now[:]
            temp.append(1)
            findAnswer(temp)
            return
    else:
        if now[-2] == 0 and now[-1] == 1:
            temp = now[:]
            temp.append(0)
            pick(temp)
            temp = now[:]
            temp.append(1)
            pick(temp)
        elif now[-2] == 1 and now[-1] == 1:
            temp = now[:]
            temp.append(0)
            pick(temp)
        elif now[-1] == 0:
            temp = now[:]
            temp.append(1)
            pick(temp)


def findAnswer(arr):
    global answer
    temp = 0
    for j in range(len(arr)):
        if arr[j] == 1:
            temp += stairsArr[j]
    if temp > answer:
        answer = temp


pick([0, 1])
pick([1, 0])
pick([1, 1])

print(answer)
