# Hashing ( 정답 )
# 알고리즘 : 문자열
# 문자를 ascii코드로 바꾼 후 해시값 계산

l = int(input())
s = input()
a = []
answer = 0
for i in s:
    a.append(ord(i)-96)

for i in range(l):
    answer = (answer + a[i]*(31**i)) % 1234567891
print(answer)
