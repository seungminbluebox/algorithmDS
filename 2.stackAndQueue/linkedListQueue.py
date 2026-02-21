class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedListQueue:
    def __init__(self):
        self.front=None
        self.rear=None

    def isEmpty(self):
        if self.front is None:
            return True
    
    def enque(self,data):
        newNode=Node(data)
        if self.rear is None:
            self.rear=self.front=newNode
            newNode.next=newNode
            return
        self.rear.next=newNode
        newNode.next=self.front
        self.rear=newNode

    def deque(self):
        if self.isEmpty():
            return False
        item=self.front.data
        self.front=self.front.next
        self.rear.next=self.front
        if self.front is None:
            self.front=self.rear=None
        return item
    
    
    def display(self):
        if self.isEmpty():
            return False
        cur=self.front
        while True:
            print(cur.data)
            cur=cur.next
            if cur==self.front:
                break
# 1. 큐 생성
my_queue = LinkedListQueue()

# 2. 데이터 삽입 테스트
print("--- 데이터 삽입 (1, 2, 3) ---")
my_queue.enque(1)
my_queue.enque(2)
my_queue.enque(3)
my_queue.display() 
# 결과: Front -> 1 -> 2 -> 3 -> (Back to Front)

# 3. 데이터 추출 테스트
print("\n--- 데이터 추출 (Pop) ---")
print(f"추출된 데이터: {my_queue.deque()}") # 1
print(f"추출된 데이터: {my_queue.deque()}") # 2

print("\n--- 현재 큐 상태 ---")
my_queue.display()
# 결과: Front -> 3 -> (Back to Front)

# 4. 마지막 노드 삭제 및 비어있는지 확인
print("\n--- 마지막 노드 삭제 ---")
my_queue.deque() # 3 삭제
my_queue.display() # none 출력