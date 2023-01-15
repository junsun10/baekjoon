# IOIOI ( 정답 100% )
# 알고리즘 : 구현
# 각 IOI 그룹 길이 저장후 한번에 계산

n = int(input())
m = int(input())
s = input()
sub = []
count = 0 if s[0] == "O" else 1
for i in range(1, m):
    if i == m-1:
        if s[i-1] == "O" and s[i] == "I":
            if count > 0:
                count += 1
                sub.append(count//2)
        elif s[i-1] == "I" and s[i] == "I":
            sub.append(count//2)
        elif s[i-1] == "I" and s[i] == "O":
            sub.append(count//2)
        else:
            if count > 1:
                sub.append((count-1//2))

    elif s[i-1] == "O" and s[i] == "I":
        count += 1
    elif s[i-1] == "I" and s[i] == "I":
        sub.append(count//2)
        count = 1
    elif s[i-1] == "I" and s[i] == "O":
        count += 1
    else:
        if count > 1:
            sub.append((count-1)//2)
            count = 0
        else:
            count = 0
answer = 0
for i in sub:
    if i >= n:
        answer += i-n+1
print(answer)
