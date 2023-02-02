# 영수증

receipt = int(input())
for _ in range(int(input())):
    a, b = map(int, input().split())
    receipt -= a*b
if receipt == 0:
    print("Yes")
else:
    print("No")
