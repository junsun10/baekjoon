# 요세푸스 문제 0 ( 정답 )
# 알고리즘 : 구현

n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
answer = []
index = 0
while len(arr) > 0:
    index = (index + k - 1) % len(arr)
    answer.append(arr[index])
    arr.remove(arr[index])

answer_s = "<"
for i in answer:
    answer_s += str(i)+", "
answer_s = answer_s[:-2]
answer_s += ">"
print(answer_s)
