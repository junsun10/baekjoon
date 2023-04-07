# 개미 ( 정답 )
# 알고리즘 : 구현, 문자열

n1, n2 = map(int, input().split())
g1 = list(input())
g2 = list(input())
state = [g1[i] for i in range(n1-1, -1, -1)] + [i for i in g2]
t = int(input())

for _ in range(t):
    new_state = []
    for i, v in enumerate(state):
        if v in g1 and i < n1+n2-1 and state[i+1] in g2:
            new_state.append(state[i+1])
            new_state.append(v)
        elif v in g2 and i > 0 and state[i-1] in g1:
            continue
        else:
            new_state.append(v)
    state = new_state[:]

print("".join(state))
