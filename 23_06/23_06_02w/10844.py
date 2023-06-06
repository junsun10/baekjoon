# 쉬운 계단 수 ( 정답 )
# 알고리즘 : dp
# 끝자리 숫자의 개수 저장
# i 일때 i-1, i+1 개수 합

n = int(input())

if n == 1:
    print(9)
else:
    list = [0]+[1 for _ in range(9)]
    for _ in range(n-1):
        new_list = [0 for _ in range(10)]
        for i in range(10):
            if i == 0:
                new_list[i] = list[i+1]
            elif i == 9:
                new_list[i] = list[i-1]
            else:
                new_list[i] = list[i-1] + list[i+1]
        list = new_list[:]
    print(sum(list) % 1000000000)
