# 줄 세우기 ( 오답 )

n, m = map(int, input().split())
group = []
check = [False for _ in range(n+1)]


def get_index(x):
    for i in range(len(group)):
        if x in group[i]:
            return i, group[i].index(x)


for _ in range(m):
    a, b = map(int, input().split())

    # 둘다 처음 등장
    if check[a] == False and check[b] == False:
        group.append([a, b])
        check[a] = True
        check[b] = True
    # b 처음 등장
    elif check[a] and check[b] == False:
        group_index, index = get_index(a)
        group[group_index] = group[group_index][:index+1] + \
            [b] + group[group_index][index+1:]
        check[b] = True
    # a 처음 등장
    elif check[a] == False and check[b]:
        group_index, index = get_index(b)
        group[group_index] = group[group_index][:index] + \
            [a] + group[group_index][index:]
        check[a] = True
    # 둘다 등장
    else:
        group_index_a, index_a = get_index(a)
        group_index_b, index_b = get_index(b)

        # 같은 그룹에 있을때
        if group_index_a == group_index_b:
            continue
        else:

            # a가 그룹에서 맨뒤일때
            if group[group_index_a][-1] == a:
                if group[group_index_b][-1] == b:
                    group[group_index_a] = group[group_index_a] + \
                        group[group_index_b]
                    group.pop(group_index_b)
                else:
                    group.append(group[group_index_b][index_b+1:])
                    group[group_index_a] = group[group_index_a] + \
                        group[group_index_b][:index_b+1]
                    group.pop(group_index_b)
            else:
                if group[group_index_b][-1] == b:
                    group.append(group[group_index_a][index_a+1:])
                    group[group_index_a] = group[group_index_a][:index_a+1] + \
                        group[group_index_b]
                    group.pop(group_index_b)
                else:
                    group.append(group[group_index_a][index_a+1:])
                    group.append(group[group_index_b][index_b+1:])
                    group[group_index_a] = group[group_index_a][:index_a+1] + \
                        group[group_index_b][:index_b+1]
                    group.pop(group_index_b)


for i in group:
    for j in i:
        print(j, end=" ")
print()
