# 재귀의 귀재 ( 정답 )
# 알고리즘 : 재귀, 문자열

def recursion(s, l, r, c):
    if l >= r:
        return 1, c+1
    elif s[l] != s[r]:
        return 0, c+1
    else:
        return recursion(s, l+1, r-1, c+1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)


for _ in range(int(input())):
    t = input()
    a, b = isPalindrome(t)
    print(a, b)
