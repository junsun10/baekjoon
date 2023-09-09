# 라라와 욕맥 변환 ( 틀림 )

n, h = map(int, input().split())
e = [i for i in input()]
arr = [h for _ in range(n)]

available = True
count = 0
index = [-1, -1, -1]


def check(i):
    if arr[index[i]] == 0:
        return True
    else:
        return False


for i in range(n):
    if e[i] == 'S':
        now = 0
    elif e[i] == 'R':
        now = 1
    else:
        now = 2

    if index[now] == -1:
        index[now] = i
    else:
        if arr[index[now]] == 0:
            index[now] = i
        # 소환되어 있는 경우
        else:
            temp = []
            for j in range(3):
                if index[j] == -1 or check(j):
                    temp.append(j)

            if len(temp) == 0:
                available = False
                break
            elif len(temp) == 1:
                index[temp[0]] = i
            else:
                if i+1 < n:
                    next_item = e[i+1]
                    if next_item == 'S':
                        next_item = 0
                    elif next_item == 'R':
                        next_item = 1
                    else:
                        next_item = 2
                    if temp[0] == next_item:
                        index[temp[1]] = i
                    elif temp[1] == next_item:
                        index[temp[0]] = i
                    else:
                        index[temp[0]] = i
                else:
                    index[temp[0]] = i
            count += 1

    for j in range(3):
        if index[j] != -1 and arr[index[j]] > 0:
            arr[index[j]] -= 1

    # print(arr)

for i in range(arr[-1]):
    for j in range(3):
        if index[j] != -1 and arr[index[j]] > 0:
            arr[index[j]] -= 1

# print("final arr")
# print(arr)

for i in range(n):
    if arr[i] != 0:
        available = False
        break

if available:
    print(count)
else:
    print(-1)
