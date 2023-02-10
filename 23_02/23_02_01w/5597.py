# 과제 안 내신 분..? ( 정답 )
# 알고리즘 : 구현

arr = [False for _ in range(31)]

for _ in range(28):
    a = int(input())
    arr[a] = True

for i in range(1, 31):
    if arr[i] == False:
        print(i)
