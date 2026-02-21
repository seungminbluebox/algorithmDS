class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedListStack:
    def __init__(self):
        self.head=None
        self.count=0
    
    def push(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        self.count+=1

    def pop(self):
        if self.isEmpty():
            return False
        item=self.head.data
        self.head=self.head.next
        self.count-=1 
        return item
    
    def peek(self):
        if self.isEmpty():
            return False
        return self.head.data
    
    def isEmpty(self):
        if  self.head is None:
            return True
        return False
    
    def getSize(self):
        return self.count
    
# 1. 스택 생성
stack = LinkedListStack()

# 2. 데이터 푸시 (1 -> 2 -> 3 순서로 쌓기)
print("--- 데이터 Push ---")
stack.push(1)
stack.push(2)
stack.push(3) # 현재 Top은 3

# 3. 현재 상태 확인
print(f"현재 스택 크기: {stack.getSize()}") # 3
print(f"맨 위 데이터(Peek): {stack.peek()}") # 3

# 4. 데이터 팝 (나중에 들어온 3부터 나옴)
print("\n--- 데이터 Pop ---")
print(f"Pop: {stack.pop()}") # 3
print(f"Pop: {stack.pop()}") # 2

# 5. 최종 확인
print(f"\n남은 데이터 개수: {stack.getSize()}") # 1
print(f"현재 Top: {stack.peek()}") # 1