# IOIOI ( 정답 50% )
# 알고리즘 : 구현

n = int(input())
m = int(input())
s = input()
p = "IO"*n+"I"
answer = 0
for i in range(0, m-2*n):
    if s[i:i+2*n+1] == p:
        answer += 1
print(answer)
