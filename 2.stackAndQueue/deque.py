class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def pushFront(self,data):
        newNode=Node(data)
        if self.front is None:
            self.front=self.rear=newNode
            newNode.next=newNode.prev=newNode
            return
        newNode.next=self.front
        newNode.prev=self.rear

        self.rear.next=newNode
        self.front.prev=newNode

        self.front=newNode

    def pushBack(self,data):
        newNode=Node(data)
        if self.rear is None:
            self.front=self.rear=newNode
            newNode.next=newNode.prev=newNode
            return
        newNode.prev=self.rear
        newNode.next=self.front

        self.rear.next=newNode
        self.front.prev=newNode

        self.rear=newNode

    def popFront(self):
        if self.front is None:
            return False
        
        data=self.front.data
        if self.front==self.rear:
            self.front=self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=self.rear
            self.rear.next=self.front
        return data
    
    def popBack(self):
        if self.rear is None:
            return False
        item=self.rear.data
        
        if self.rear==self.front:
            self.rear=self.front=None
        
        else:
            self.rear=self.rear.prev
            self.rear.next=self.front
            self.front.prev=self.rear

        return item
    
    def peekFront(self):
        if  self.front:
            return self.front.data
        else:
            return False

    def peekBack(self):
        if self.rear:
            return self.rear.data
        else:
            return False 
        
# 1. 데크 인스턴스 생성
my_deque = Deque()

# 2. 데이터 삽입 테스트
print("--- 데이터 삽입 ---")
my_deque.pushBack(10)   # [10]
my_deque.pushFront(5)   # [5, 10]
my_deque.pushBack(20)   # [5, 10, 20]

print(f"Front 데이터: {my_deque.peekFront()}") # 5
print(f"Rear 데이터: {my_deque.peekBack()}")   # 20

# 3. 데이터 추출 테스트 (FIFO 및 LIFO 복합)
print("\n--- 데이터 추출 ---")
print(f"popFront 실행: {my_deque.popFront()}") # 5 추출
print(f"popBack 실행: {my_deque.popBack()}")   # 20 추출

# 4. 남은 데이터 및 최종 추출
print("\n--- 최종 상태 확인 ---")
print(f"현재 남은 데이터 (Peek): {my_deque.peekFront()}") # 10
print(f"마지막 데이터 추출: {my_deque.popFront()}")      # 10 추출
print(f"비어있는 데크 pop 시도: {my_deque.popFront()}")   # False 반환