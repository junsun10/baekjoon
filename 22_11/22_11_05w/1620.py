# 나는야 포켓몬 마스터 이다솜 ( 정답 )
# 알고리즘 : 해시
# 포켓몬스터의 번호와 이름으로 딕셔너리 생성

import sys

n, m = map(int, input().split())

dic1 = {0: ""}
dic2 = {"": 0}


def isNumber(x):
    for i in range(10):
        if str(i) in x:
            return True
    return False


for i in range(1, n+1):
    name = sys.stdin.readline()
    dic1[i] = name[:-1]
    dic2[name] = i
for i in range(m):
    question = sys.stdin.readline()
    if isNumber(question):
        print(dic1.get(int(question)))
    else:
        print(dic2.get(question))
