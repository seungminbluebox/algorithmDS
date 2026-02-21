class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class Circle:
    def __init__(self):
        self.head=None #tail은 head의 prev이기때문에 굳이 작성 안함
        self.current=None

    def insertAtHead(self,data):
        newNode=Node(data)
        if not self.head:
            newNode.next=newNode.prev=newNode
            self.current=self.head=newNode
            return
        tail=self.head.prev

        newNode.next=self.head #current아니라 head
        newNode.prev=tail

        tail.next=newNode
        self.head.prev=newNode #current아니라 head

        self.head=newNode    
    def insertAtTail(self,data):
        newNode=Node(data)
        if not self.head:
            newNode.next=newNode.prev=newNode
            self.head=self.current=newNode
            return
        tail=self.head.prev

        newNode.next=self.head
        newNode.prev=tail

        tail.next=newNode
        self.head.prev=newNode

        tail=newNode
    def deleteFromHead(self):
        if not self.head:
            return
        if self.head==self.head.prev:
            self.head=self.current=None
            return
        tail=self.head.prev
        self.head=self.head.next
        self.head.prev=tail
        tail.next=self.head
        self.current=self.head
        
    
    def deleteFromTail(self):
        if not self.head:
            return
        if self.head==self.head.prev:
            self.head=self.current=None
            return
        tail=self.head.prev
        tail=tail.prev
        self.head.prev=tail
        tail.next=self.head
        self.current=tail

    def moveFoward(self):
        if self.current:
            self.current=self.current.next
    
    def moveBack(self):
        if self.current:
            self.current=self.current.prev
    
    def printCurrent(self):
        if self.current:
            print(self.current.data)
            return
        else:
            return
        

    def travFoward(self):
        if not self.head:
            return
        cur=self.head
        while True:
            print(cur.data)
            cur=cur.next
            if cur==self.head:
                break

        
    
    def travBack(self):
        if not self.head:
            return
        cur=self.head.prev
        while True:
            print(cur.data)
            cur=cur.prev
            if cur==self.head.prev:
                break

# --- [위의 클래스 정의들은 생략, 출력 부분만 .data로 수정했다고 가정] ---

# 1. 리스트 생성
my_list = Circle()

# 2. 데이터 삽입 테스트
print("--- 삽입 테스트 ---")
my_list.insertAtHead(20)  # [20]
my_list.insertAtHead(10)  # [10, 20]
my_list.insertAtTail(30)  # [10, 20, 30]

print("정방향 순회:", end=" ")
my_list.travFoward() # 10 -> 20 -> 30

# 3. 현재 위치 이동 테스트
print("\n--- 이동 테스트 ---")
my_list.printCurrent() # 10 (첫 삽입 시 head였으므로)
my_list.moveFoward()
my_list.printCurrent() # 20
my_list.moveBack()
my_list.printCurrent() # 10

# 4. 삭제 테스트
print("\n--- 삭제 테스트 ---")
my_list.deleteFromHead() # 10 삭제
print("Head 삭제 후:", end=" ")
my_list.travFoward()    # 20 -> 30

my_list.deleteFromTail() # 30 삭제
print("Tail 삭제 후:", end=" ")
my_list.travFoward()    # 20 (하나 남음)

# 5. 역방향 순회 테스트
print("\n--- 역방향 순회 ---")
my_list.insertAtTail(40)
my_list.insertAtTail(50)
print("현재 리스트:", end=" ")
my_list.travFoward()    # 20 -> 40 -> 50
print("역방향 순회:", end=" ")
my_list.travBack()      # 50 -> 40 -> 20