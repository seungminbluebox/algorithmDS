class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
class BST:
    def insert(self,node,data):
        if not node:
            return Node(data)
        if node.data>data:
            node.left=self.insert(node.left,data)
        elif node.data<data:
            node.right=self.insert(node.right,data)
        return node
    
    def search(self,node,data):
        if not node or node.data==data:
            return node
        if node.data>data:
            return self.search(node.left,data)
        elif node.data<data:
            return self.search(node.right,data)
    def findMin(self,node):
        if not node:
            return False
        current=node
        while current.left:
            current=current.left
        return current

    def delete(self,node,data):
        if not node:
            return node
        if node.data>data:
            node.left=self.delete(node.left,data)
        elif node.data<data:
            node.right=self.delete(node.right,data)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp=self.findMin(node.right)
            node.data=temp.data
            node.right=self.delete(node.right,temp.data)
        return node
    
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

tree = BST()
root = None # 처음 트리는 비어있습니다.

# 2. 데이터 삽입 (우리가 예시로 들었던 트리 구조 생성)
# 트리에 변화가 생길 때마다 반환값을 다시 root에 덮어씌워 구조를 유지합니다.
root = tree.insert(root, 10)
root = tree.insert(root, 5)
root = tree.insert(root, 2)
root = tree.insert(root, 6)
root = tree.insert(root, 3)

print("삽입 완료 후 중위 순회 결과 (정렬되어 출력되어야 정상):")
tree.inorder(root)
print("\n" + "-" * 30)

# 3. 데이터 탐색
search_result = tree.search(root, 3)
if search_result:
    print(f"탐색 성공: 노드 값 {search_result.data}을(를) 찾았습니다.")
else:
    print("탐색 실패: 값을 찾지 못했습니다.")
print("-" * 30)

# 4. 데이터 삭제 (가장 까다로운 자식이 둘 달린 노드 5 삭제)
print("노드 5 삭제 진행 중...")
root = tree.delete(root, 5)

print("삭제 완료 후 중위 순회 결과 (5가 사라지고 구조가 유지되어야 정상):")
tree.inorder(root)