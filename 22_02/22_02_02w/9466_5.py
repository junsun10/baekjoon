# 텀 프로젝트 ( 정답 )

# 이전 버전들에서는 find를 너무 복잡하게 만든듯


import sys
sys.setrecursionlimit(111111)

def find(x):
    global group
    visited[x] = True
    arr.append(x)

    if visited[s[x]] == True:
        if s[x] in arr:
            group += arr[arr.index(s[x]):]
        return
    else:
        find(s[x])


# T 입력
t = int(sys.stdin.readline())
for _ in range(t):

    # 학생수, 선택한 학생 배열 입력
    n = int(sys.stdin.readline())
    s = list(map(int,sys.stdin.readline().split()))
    s = [0] + s

    # 방문 여부
    visited=[False for _ in range(n+1)]

    # 그룹 만든 사람들
    group = []
    
    
    for i in range(1,n+1):                                               
        if visited[i] == True:
            continue
        else:
            arr = []
            find(i)                                   


    print(n-len(group))

