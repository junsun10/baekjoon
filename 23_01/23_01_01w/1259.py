# 팰린드롬수 ( 정답 )
# 알고리즘 : 구현

while True:
    s = input()
    p = False
    if s == "0":
        break
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            print("no")
            p = True
            break
    if not p:
        print("yes")
