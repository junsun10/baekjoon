# 톱니바퀴 ( 정답 )
# 입력받은 배열은 그대로 두고
# 3시, 9시방향 톱니 인덱스를 바꾸면서 계산

import sys
ssr = sys.stdin.readline

LEFT = 0
RIGHT = 1

g = []
s = [[6,2],[6,2],[6,2],[6,2]]
for _ in range(4):
    temp = []
    temp = list(map(int,ssr().strip()))
    g.append(temp)
# print(g)

k = int(ssr())

for _ in range(k):
    g_num, spin = map(int,ssr().split())

    if g_num == 1:
        if g[0][s[0][RIGHT]] != g[1][s[1][LEFT]]:
            if g[1][s[1][RIGHT]] != g[2][s[2][LEFT]]:
                if g[2][s[2][RIGHT]] != g[3][s[3][LEFT]]:
                    s[0][RIGHT] -= spin
                    s[1][LEFT] += spin
                    s[1][RIGHT] += spin
                    s[2][LEFT] -= spin
                    s[2][RIGHT] -= spin
                    s[3][LEFT] += spin
                else:
                    s[0][RIGHT] -= spin
                    s[1][LEFT] += spin
                    s[1][RIGHT] += spin
                    s[2][LEFT] -= spin
                    s[2][RIGHT] -= spin
            else:
                s[0][RIGHT] -= spin
                s[1][LEFT] += spin
                s[1][RIGHT] += spin
        else:
            s[0][RIGHT] -= spin
    
    if g_num == 2:
        if g[0][s[0][RIGHT]] != g[1][s[1][LEFT]]:
            s[0][RIGHT] += spin
        if g[1][s[1][RIGHT]] != g[2][s[2][LEFT]]:
            if g[2][s[2][RIGHT]] != g[3][s[3][LEFT]]:
                s[1][LEFT] -= spin
                s[1][RIGHT] -= spin
                s[2][LEFT] += spin
                s[2][RIGHT] += spin
                s[3][LEFT] -= spin
            else:
                s[1][LEFT] -= spin
                s[1][RIGHT] -= spin
                s[2][LEFT] += spin
                s[2][RIGHT] += spin
        else:
            s[1][LEFT] -= spin
            s[1][RIGHT] -= spin
    
    if g_num == 3:
        if g[2][s[2][RIGHT]] != g[3][s[3][LEFT]]:
            s[3][LEFT] += spin
        if g[1][s[1][RIGHT]] != g[2][s[2][LEFT]]:
            if g[0][s[0][RIGHT]] != g[1][s[1][LEFT]]:
                s[0][RIGHT] -= spin
                s[1][LEFT] += spin
                s[1][RIGHT] += spin
                s[2][LEFT] -= spin
                s[2][RIGHT] -= spin
            else:
                s[1][LEFT] += spin
                s[1][RIGHT] += spin
                s[2][LEFT] -= spin
                s[2][RIGHT] -= spin
        else:
            s[2][LEFT] -= spin
            s[2][RIGHT] -= spin
    
    if g_num == 4:
        if g[2][s[2][RIGHT]] != g[3][s[3][LEFT]]:
            if g[1][s[1][RIGHT]] != g[2][s[2][LEFT]]:
                if g[0][s[0][RIGHT]] != g[1][s[1][LEFT]]:
                    s[0][RIGHT] += spin
                    s[1][LEFT] -= spin
                    s[1][RIGHT] -= spin
                    s[2][LEFT] += spin
                    s[2][RIGHT] += spin
                    s[3][LEFT] -= spin
                else:
                    s[1][LEFT] -= spin
                    s[1][RIGHT] -= spin
                    s[2][LEFT] += spin
                    s[2][RIGHT] += spin
                    s[3][LEFT] -= spin
            else:
                s[2][LEFT] += spin
                s[2][RIGHT] += spin
                s[3][LEFT] -= spin
        else:
            s[3][LEFT] -= spin

    # 인덱스 범위 초과 방지
    for i in range(4):
        if s[i][0] == 8:
            s[i][0] = 0
        if s[i][0] == -1:
            s[i][0] = 7
        if s[i][1] == 8:
            s[i][1] = 0
        if s[i][1] == -1:
            s[i][1] = 7
    

    # print(s)
    # print()

# 점수 계산
answer = 0
if s[0][RIGHT] == 0 or s[0][RIGHT] == 1:
    if g[0][6+s[0][RIGHT]] == 1:
        answer += 1
else:
    if g[0][s[0][RIGHT]-2] == 1:
        answer += 1


if s[1][RIGHT] == 0 or s[1][RIGHT] == 1:
    if g[1][6+s[1][RIGHT]] == 1:
        answer += 2
else:
    if g[1][s[1][RIGHT]-2] == 1:
        answer += 2


if s[2][RIGHT] == 0 or s[2][RIGHT] == 1:
    if g[2][6+s[2][RIGHT]] == 1:
        answer += 4
else:
    if g[2][s[2][RIGHT]-2] == 1:
        answer += 4


if s[3][LEFT] == 6 or s[3][LEFT] == 7:
    if g[3][s[3][LEFT]-6] == 1:
        answer += 8
else:
    if g[3][s[3][LEFT]+2] == 1:
        answer += 8

print(answer)