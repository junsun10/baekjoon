# 리모컨 ( 틀림 )

import itertools

n = input()
lenN = len(n)
n = int(n)
m = int(input())
# 고장난 버튼 없는 경우
if m == 0:
    # +,-가 빠른 경우
    if lenN > abs(n-100):
        print(abs(n-100))
    else:
        print(lenN)
else:
    arr = list(map(int, input().split()))
    available = []
    nums = []
    answer1 = 500001
    answer2 = 500001
    answer3 = 500001
    # 이동할 채널이 100인 경우
    if n == 100:
        print(0)
    # 버튼이 전부 고장난 경우
    elif m == 10:
        print(abs(n-100))
    else:
        for i in range(10):
            if i not in arr:
                available.append(i)
        nums = list(itertools.product(available, repeat=lenN))
        answerNum = -1
        for num in nums:
            temp = 0
            for x in range(len(num)):
                temp += num[x]*(10**(len(num)-1-x))
            if abs(n-temp) < abs(n-answerNum):
                answerNum = temp
        answer1 = lenN + abs(n-answerNum)

        nums2 = list(itertools.product(available, repeat=lenN+1))
        answerNum = -1
        for num in nums2:
            temp = 0
            for x in range(len(num)):
                temp += num[x]*(10**(len(num)-1-x))
            if abs(n-temp) < abs(n-answerNum):
                answerNum = temp
        answer2 = lenN + 1 + abs(n-answerNum)

        if lenN > 1:
            nums3 = list(itertools.product(available, repeat=lenN-1))
            answerNum = -1
            for num in nums3:
                temp = 0
                for x in range(len(num)):
                    temp += num[x]*(10**(len(num)-1-x))
                if abs(n-temp) < abs(n-answerNum):
                    answerNum = temp
            answer3 = lenN - 1 + abs(n-answerNum)

        answer = min(answer1, answer2, answer3)

        if answer > abs(n-100):
            print(abs(n-100))
        else:
            print(answer)
