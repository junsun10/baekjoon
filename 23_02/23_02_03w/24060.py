# 알고리즘 수업 - 병합 정렬 1 ( 정답 )
# 알고리즘 : 정렬, 재귀

n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
answer = -1


def merge(a, p, q, r):
    global count, answer
    i, j, t = p, q+1, 0
    tmp = []
    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            t += 1
            i += 1
        else:
            tmp.append(a[j])
            t += 1
            j += 1

    while i <= q:
        tmp.append(a[i])
        t += 1
        i += 1

    while j <= r:
        tmp.append(a[j])
        t += 1
        j += 1

    i, t = p, 0
    while i <= r:
        count += 1
        if count == k:
            answer = tmp[t]
        a[i] = tmp[t]
        i += 1
        t += 1


def merge_sort(a, p, r):
    if p < r:
        q = (p + r)//2
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)


merge_sort(arr, 0, n-1)
print(answer)
