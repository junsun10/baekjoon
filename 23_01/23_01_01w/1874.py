# 스택 수열 ( 정답 )
# 알고리즘 : 스택
# 입력받은 수열과 스택 비교
# 스택에 값이 남아있으면 불가능

from collections import deque

n = int(input())
arr = deque()
for i in range(n):
    arr.appendleft(int(input()))
stack = deque()
count = 0
answer = []
for i in range(1, n+1):
    stack.append(i)
    answer.append("+")
    while len(stack) > 0 and arr[-1] == stack[-1]:
        arr.pop()
        stack.pop()
        answer.append("-")
if len(arr) > 0:
    print("NO")
else:
    for i in answer:
        print(i)
