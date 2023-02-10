# 트리 순회 ( 정답 )
# 알고리즘 : 트리

class node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_left(self, child):
        self.left = child

    def add_right(self, child):
        self.right = child

    def preorder_traversal(self):
        print(self.value, end="")
        if self.left != None:
            self.left.preorder_traversal()
        if self.right != None:
            self.right.preorder_traversal()

    def inorder_traversal(self):
        if self.left != None:
            self.left.inorder_traversal()
        print(self.value, end="")
        if self.right != None:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        if self.left != None:
            self.left.postorder_traversal()
        if self.right != None:
            self.right.postorder_traversal()
        print(self.value, end="")


arr = []
dict = {}
for _ in range(int(input())):
    x, y, z = map(str, input().split())
    arr.append((x, y, z))
    dict[x] = node(x)

for x, y, z in arr:
    if y != ".":
        dict[x].add_left(dict[y])
    if z != ".":
        dict[x].add_right(dict[z])

root = dict["A"]
root.preorder_traversal()
print()
root.inorder_traversal()
print()
root.postorder_traversal()
print()
