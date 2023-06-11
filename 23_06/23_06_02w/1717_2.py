# 집합의 표현 ( 시간 초과 )

n, m = map(int, input().split())

n_dict = {}
count = 0

for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        if a not in n_dict and b not in n_dict:
            n_dict[a] = count
            n_dict[b] = count
            count += 1
        elif a not in n_dict and b in n_dict:
            n_dict[a] = n_dict[b]
        elif a in n_dict and b not in n_dict:
            n_dict[b] = n_dict[a]
        else:
            now_a = n_dict[a]
            now_b = n_dict[b]
            for key, value in n_dict.items():
                if value == now_b:
                    n_dict[key] = now_a
    else:
        if a in n_dict and b in n_dict and n_dict[a] == n_dict[b]:
            print("YES")
        else:
            print("NO")
