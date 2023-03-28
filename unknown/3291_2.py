# LIST

n = int(input())
available = [[i] for i in range(n)]
block = [False for _ in range(n)]
check = {}
list = ["" for _ in range(n)]
answer = []

for i in range(n):
    name = input()
    state = input()
    check[name] = False

    if state == "UP":
        for j in range(i+1, n):
            if block[j]:
                continue
            available[j].append(name)
    elif state == "DOWN":
        for j in range(i):
            if block[j]:
                continue
            available[j].append(name)
    else:
        available[j] = [name]
        block[j] = True

for i in range(n):
    available[i] = [len(available[i])] + available[i]

print(available)
available.sort(reverse=True)
print(available)


def dfs(x):
    global answer
    print(list)
    if len(answer) > 0:
        return

    if x == n:
        answer = list[:]
        return

    for i in range(2, len(available[x])):
        if check[available[x][i]] == False:
            list[available[x][1]] = available[x][i]
            check[available[x][i]] = True
            dfs(x+1)
            check[available[x][i]] = False


dfs(0)
for i in answer:
    print(i)
