class CircularQueue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.queue=[None]*capacity
        self.front=0
        self.rear=0
        self.size=0

    def is_empty(self):
        if self.size==0:
            return True
        return False
    
    def is_full(self):
        if self.size==self.capacity:
            return True
        return False
    
    def enqueue(self,data):
        if self.is_full():
            return False
        self.queue[self.rear]=data
        self.rear=(self.rear+1)%self.capacity
        self.size+=1

    def dequeue(self):
        if self.is_empty():
            return False
        item=self.queue[self.front]
        self.queue[self.front]=None
        self.front=(self.front+1)%self.capacity
        self.size-=1
        return item
    
    def display(self):
        if self.is_empty():
            return False
        curr=self.front
        for i in range(self.size):
            print(self.queue[curr])
            curr=(curr+1)%self.capacity
# 1. 용량이 5인 원형 큐 생성
cq = CircularQueue(5)

print("--- 1. 데이터 삽입 (10, 20, 30) ---")
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()  # 결과: 10, 20, 30 순서로 출력

print("\n--- 2. 데이터 2개 삭제 (10, 20 추출) ---")
print(f"삭제된 데이터: {cq.dequeue()}")
print(f"삭제된 데이터: {cq.dequeue()}")
cq.display()  # 결과: 30만 남음

print("\n--- 3. 원형 회전 테스트 (40, 50, 60, 70 삽입) ---")
# 현재 front는 2에 있고, 뒤쪽에 빈 공간이 생겼으므로 회전하며 채워집니다.
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)
cq.enqueue(70)
cq.display()  # 결과: 30, 40, 50, 60, 70 순서로 출력

print("\n--- 4. 가득 찬 상태 테스트 ---")
# 이미 5개가 꽉 찼으므로 False를 반환하거나 메시지가 뜰 것입니다.
is_success = cq.enqueue(80)
if is_success == False:
    print("큐가 꽉 차서 80을 넣지 못했습니다.")

print("\n--- 5. 최종 큐 상태 및 크기 확인 ---")
print(f"현재 데이터 개수: {cq.size}")
cq.display()