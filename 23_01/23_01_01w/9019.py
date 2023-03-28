# DSLR

from collections import deque


def get_d(n):
    arr = deque()
    while n > 0:
        arr.appendleft(n % 10)
        n = n//10
    while len(arr) < 4:
        arr.appendleft(0)
    return arr


for _ in range(int(input())):
    answer = []
    a, b = map(int, input().split())
    queue = deque()
    queue.append([a, 0, ""])
    end = False

    arr1 = get_d(a)
    arr2 = get_d(a)
    for k in range(3):
        arr1.rotate()
        temp = 0
        for i in range(4):
            temp += arr1[i]*(10**(3-i))
        if temp == b:
            print("R"*(k+1))
            end = True
            break
        arr2.rotate(-1)
        temp = 0
        for i in range(4):
            temp += arr2[i]*(10**(3-i))
        if temp == b:
            print("L"*(k+1))
            end = True
            break
    if end:
        continue

    visited = [a]
    while queue:
        now, count, l = queue.popleft()

        if now == b:
            print(l)
            break

        temp = now
        temp = temp*2 % 10000
        if temp not in visited:
            visited.append(temp)
        queue.append([temp, count+1, l+"D"])

        temp = now
        temp -= 1
        if temp == 0:
            temp = 9999
        if temp not in visited:
            visited.append(temp)
        queue.append([temp, count+1, l+"S"])

        if len(l) == 0 or (len(l) > 0 and l[-1] != "R"):
            arr = get_d(now)
            new_arr = [arr[1], arr[2], arr[3], arr[0]]
            temp = 0
            for i in range(4):
                temp += new_arr[i]*(10**(3-i))
            if temp not in visited:
                visited.append(temp)
            queue.append([temp, count+1, l+"L"])

        if len(l) == 0 or (len(l) > 0 and l[-1] != "L"):
            arr = get_d(now)
            new_arr = [arr[3], arr[0], arr[1], arr[2]]
            temp = 0
            for i in range(4):
                temp += new_arr[i]*(10**(3-i))
            if temp not in visited:
                visited.append(temp)
            queue.append([temp, count+1, l+"R"])
