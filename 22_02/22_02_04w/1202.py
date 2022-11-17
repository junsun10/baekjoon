# 보석 도둑 ( 시간초과 )
# 보석은 내림차순 가방은 오름차순해서 하나씩 넣음

from audioop import reverse
from operator import itemgetter
import sys

# n: 보석개수 k: 가방개수
n,k = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

b = [int(sys.stdin.readline()) for _ in range(k)]
b.sort()
is_b = [False for _ in range(k)]

s_arr = sorted(arr,key=itemgetter(1),reverse=True)

answer = 0
for i in range(n):
    for j in range(k):  
        if is_b[j]==True:
            continue
        elif s_arr[i][0]<=b[j]:
            # print(s_arr[i][0],b[j])
            is_b[j]=True
            answer += s_arr[i][1]
            break
        else:
            continue
        
# print(s_arr)
# print(is_b)
print(answer)