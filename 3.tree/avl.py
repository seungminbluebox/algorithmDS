class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1

class AVL:
    def getHeight(self,node):
        if node:
            return node.height
        else:
            return 0
    
    def getBalance(self,node):
        if not node:
            return 0
        else:
            return self.getHeight(node.left)-self.getHeight(node.right)
        
    def rotateRight(self,x):
        y=x.left
        z=y.right
        y.right=x
        x.left=z
        x.height=1+max(self.getHeight(x.left),self.getHeight(x.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    
    def rotateLeft(self,x):
        y=x.right
        z=y.left
        y.left=x
        x.right=z
        x.height=1+max(self.getHeight(x.left),self.getHeight(x.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    
    def insert(self,node,data):
        if not node:
            return Node(data)
        if node.data>data:
            node.left=self.insert(node.left,data)
        elif node.data<data:
            node.right=self.insert(node.right,data)
        else:
            return node
        node.height=1+max(self.getHeight(node.left),self.getHeight(node.right))
        balance=self.getBalance(node)

        if balance>1:
            if data<node.left.data:
                return self.rotateRight(node)
            else:
                node.left=self.rotateLeft(node.left)
                return self.rotateRight(node)
        elif balance<-1:
            if data>node.right.data:
                return self.rotateLeft(node)
            else:
                node.right=self.rotateRight(node.right)
                return self.rotateLeft(node)
        return node
    
    def getMin(self,node):
        curr=node
        while curr.left:
            curr=curr.left
        return curr
    
    def delete(self,node,data):
        if not node:
            return node
        if data<node.data:
            node.left=self.delete(node.left,data)
        elif data>node.data:
            node.right=self.delete(node.right,data)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp=self.getMin(node.right)   
            node.data=temp.data
            node.right=self.delete(node.right,temp.data)
        
        node.height=1+max(self.getHeight(node.left),self.getHeight(node.right))
        balance=self.getBalance(node)

        if balance>1:
            if self.getBalance(node.left)>=0:
                return self.rotateRight(node)
            else:
                node.left=self.rotateLeft(node.left)
                return self.rotateRight(node)
        elif balance<-1:
            if self.getBalance(node.right)<=0:
                return self.rotateLeft(node)
            else:
                node.right=self.rotateRight(node.right)
                return self.rotateLeft(node)
        return node
    
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)


# 1. 트리 객체 생성 및 초기 루트 노드 설정
my_tree = AVL()
root = None

# 2. 데이터 삽입 테스트 (불균형 유발 및 자가 균형 증명)
# 10, 20, 30을 순서대로 넣으면 RR 불균형이 발생하고 스스로 좌회전해야 정상입니다.
print("- 데이터 삽입 시작 -")
data_list = [10, 20, 30, 40, 50, 25]
for data in data_list:
    root = my_tree.insert(root, data)
    print(f"삽입 완료: {data}")

# 중위 순회 결과 출력 (이진 탐색 트리 규칙에 따라 무조건 오름차순이어야 함)
print("\n- 삽입 후 중위 순회 (정렬 확인) -")
my_tree.inorder(root)

# 객관적 구조 확인: 루트 노드가 무엇인지 확인 (단순 삽입이었다면 10이어야 하지만, AVL은 30을 루트로 끌어올려 균형을 맞춥니다)
print(f"\n현재 루트 노드의 데이터: {root.data}")
print(f"현재 루트 노드의 높이: {root.height}")

# 3. 데이터 삭제 테스트
# 자식이 두 개 있는 까다로운 노드(예: 30)를 삭제해 봅니다.
delete_target = 30
print(f"\n- 데이터 {delete_target} 삭제 시작 -")
root = my_tree.delete(root, delete_target)

print("- 삭제 후 중위 순회 (구조 유지 확인) -")
my_tree.inorder(root)