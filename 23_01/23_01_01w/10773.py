# 제로 ( 정답 )
# 알고리즘 : 스택


arr = []
k = int(input())
for _ in range(k):
    m = int(input())
    if m != 0:
        arr.append(m)
    else:
        arr.pop()
print(sum(arr))
