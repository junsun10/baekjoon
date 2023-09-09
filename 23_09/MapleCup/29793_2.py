# 라라와 용맥 변환 ( 시간초과 )

from collections import deque


n, h = map(int, input().split())
e = [i for i in input()]
arr = [h for _ in range(n)]

answer = n


dq = deque()
dq.append(([h for _ in range(n)], [-1, -1, -1], 0, 0))


def attack(index, arr):
    new_arr = arr[:]
    for i in range(3):
        if index[i] != -1 and new_arr[index[i]] > 0:
            new_arr[index[i]] -= 1
    return new_arr


def check(i, index, arr):
    if arr[index[i]] == 0:
        return True
    else:
        return False


while dq:
    # print(dq)
    status, index, now_index, count = dq.popleft()

    if now_index == n:
        for i in range(status[-1]):
            for j in range(3):
                if index[j] != -1 and status[index[j]] > 0:
                    status[index[j]] -= 1

        failed = False
        for i in range(n):
            if status[i] != 0:
                failed = True
                break

        if not failed:
            answer = min(count, answer)
            break
        continue

    if e[now_index] == 'S':
        value = 0
    elif e[now_index] == 'R':
        value = 1
    else:
        value = 2

    if index[value] == -1 or check(value, index, status):
        index[value] = now_index
        dq.append((attack(index, status), index, now_index+1, count))
    else:
        temp = []
        for i in range(3):
            if index[i] == -1 or check(i, index, status):
                temp.append(i)

        if len(temp) == 0:
            continue
        elif len(temp) == 1:
            index[temp[0]] = now_index
            dq.append((attack(index, status), index, now_index+1, count+1))
        else:
            if now_index + 1 < n:
                next_item = e[now_index+1]
                if next_item == 'S':
                    next_item = 0
                elif next_item == 'R':
                    next_item = 1
                else:
                    next_item = 2

            if temp[0] == next_item:
                index[temp[1]] = now_index
                dq.append((attack(index, status), index, now_index+1, count+1))
            elif temp[1] == next_item:
                index[temp[0]] = now_index
                dq.append((attack(index, status), index, now_index+1, count+1))
            else:
                temp1 = index[:]
                temp1[temp[0]] = now_index
                dq.append((attack(temp1, status), temp1, now_index+1, count+1))
                temp1 = index[:]
                temp1[temp[1]] = now_index
                dq.append((attack(temp1, status), temp1, now_index+1, count+1))


if answer != n:
    print(answer)
else:
    print(-1)
