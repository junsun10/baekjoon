# 오르막 수 ( 정답 )
# 알고리즘 : dp
# 마지막 자리수의 숫자별 개수를 기억해 경우의 수 계산

n = int(input())

dict = {}
for i in range(10):
    dict[i] = 1

for i in range(n-1):

    new_dict = {}
    for j in range(10):
        new_dict[j] = dict[j]

    # ex) 0 개수만큼 1~9에 더함
    for j in range(10):
        for k in range(j+1, 10):
            new_dict[k] += dict[j]

    for j in range(10):
        dict[j] = new_dict[j]

print(sum(dict.values()) % 10007)
