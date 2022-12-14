# 비밀번호 찾기 ( 정답 )
# 알고리즘 : 딕셔너리
# 주소를 키, 비밀번호를 값으로 저장

import sys

pwDict = dict()
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    url, pw = map(str, sys.stdin.readline().split())
    pwDict[url] = pw
for _ in range(m):
    url = sys.stdin.readline()
    print(pwDict[url[:-1]])
