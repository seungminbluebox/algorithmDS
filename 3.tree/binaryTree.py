from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

    def preorder(self,node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)
    def levelorder(self,node):
        if not node:
            return
        queue=deque([node])

        while queue:
            current=queue.popleft()
            print(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


# 1. 노드 생성
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

# 2. 순회 실행
print("--- 이진 트리 순회 결과 ---")

print("Preorder   :", end=" ")
root.preorder(root)   # 결과: A B D E C
print("\nInorder    :", end=" ")
root.inorder(root)    # 결과: D B E A C
print("\nPostorder  :", end=" ")
root.postorder(root)  # 결과: D E B C A
print("\nLevelorder :", end=" ")
root.levelorder(root) # 결과: A B C D E