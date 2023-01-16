# 랜선 자르기 ( 정답 )
# 알고리즘 : 이분탐색


k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]
left = 1
right = max(lans)
length = (left + right)//2


def get_count(l):
    count = 0
    for i in lans:
        count += i//l
    return count


while True:
    count = get_count(length)
    # print(length, left, right)
    if count >= n:
        left = length
        length = (left + right)//2
    else:
        right = length - 1
        length = (left + right)//2

    if left == right:
        break
    elif left+1 == right:
        temp_count = get_count(right)
        if temp_count >= n:
            length = right
        break

print(length)
