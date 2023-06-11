# 집합의 표현 ( 메모리 초과 )

n, m = map(int, input().split())

n_dict = {}
for i in range(n+1):
    n_dict[i] = -1
count = 0

for _ in range(m):
    print(n_dict)
    x, a, b = map(int, input().split())
    if x == 0:
        if n_dict[a] == -1 and n_dict[b] == -1:
            n_dict[a] = count
            n_dict[b] = count
            count += 1
        elif n_dict[a] == -1 and n_dict[b] != -1:
            n_dict[a] = n_dict[b]
        elif n_dict[a] != -1 and n_dict[b] == -1:
            n_dict[b] = n_dict[a]
        else:
            now_a = n_dict[a]
            now_b = n_dict[b]
            for i in range(n+1):
                if n_dict[i] == now_b:
                    n_dict[i] = now_a
    else:
        if n_dict[a] == n_dict[b] and n_dict[a] != -1:
            print("YES")
        else:
            print("NO")
