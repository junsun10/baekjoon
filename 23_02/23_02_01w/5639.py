# 이진 검색 트리 ( 정답 )
# 알고리즘 : 트리, 재귀
# 노드를 구현한 뒤 후위순회 구현
# 최대 input 개수만 정해져 있어서 input 받을 때 예외처리 필요했음

import sys
sys.setrecursionlimit(15000)


class node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, child):
        if child.value < self.value and self.left:
            self.left.add(child)
        elif child.value > self.value and self.right:
            self.right.add(child)
        elif child.value < self.value and self.left == None:
            self.left = child
        else:
            self.right = child

# 후위순회


def read(node):
    if node.left:
        read(node.left)
    if node.right:
        read(node.right)
    print(node.value)


v = sys.stdin.readline()
root = node(int(v[:-1]))

# input 예외 처리
while True:
    try:
        v = sys.stdin.readline()
        temp = node(int(v[:-1]))
        root.add(temp)
    except Exception:
        break

read(root)
