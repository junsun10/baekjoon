# 임스의 메이플컵 ( 정답 )
# 알고리즘: 구현

n, u, l = map(int, input().split())

answer1 = False
answer2 = False
if n >= 1000:
    answer1 = True
if u >= 8000 or l >= 260:
    answer2 = True

if answer1 and answer2:
    print("Very Good")
elif answer1:
    print("Good")
else:
    print("Bad")
