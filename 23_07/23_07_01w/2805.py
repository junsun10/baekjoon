# 나무 자르기 ( 정답 )
# 알고리즘 : 매개변수 탐색, 이분 탐색
# 아래 풀이는 매개변수 탐색
# 전체 나무의 높이를 더한 뒤 높이 1부터 시작해 목표 길이보다 낮아지는 위치 탐색

n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()
total = sum(trees)
height = 1
min_tree_index = 0
count_tree = n
answer = 0

while True:
    # 현재 자르는 높이보다 큰 나무들만 total에서 빼야 함
    if height > trees[min_tree_index]:
        min_tree_index += 1
        count_tree -= 1
        while True:
            if trees[min_tree_index-1] == trees[min_tree_index]:
                min_tree_index += 1
                count_tree -= 1
            else:
                break
    total -= count_tree

    if total < m:
        answer = height-1
        break
    else:
        height += 1

print(answer)
