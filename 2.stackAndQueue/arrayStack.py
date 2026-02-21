class ArrayStack:
    def __init__(self,size):
        self.stack=[None]*size
        self.top=-1
        self.size=size
    
    def push(self, data):
        if self.top+1==self.size:
            return
        self.top=self.top+1
        self.stack[self.top]=data

    def pop(self):
        if self.isEmpty():
            return False
        item=self.stack[self.top]
        self.stack[self.top] = None
        self.top=self.top-1
        return item
    
    def peek(self):
        if self.isEmpty():
            return False
        item=self.stack[self.top]
        return item

    def isEmpty(self):
        if self.top==-1:
            return True
        return False

    def get_size(self):
        return self.top+1        

# 1. 크기가 3인 스택 생성
my_stack = ArrayStack(3)

# 2. 데이터 삽입 (Push)
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
my_stack.push("D") # "Stack Overflow" 출력됨

# 3. 현재 상태 확인
print(f"현재 데이터 개수: {my_stack.get_size()}") # 3
print(f"맨 위 데이터(Peek): {my_stack.peek()}") # C

# 4. 데이터 추출 (Pop)
print(f"추출된 데이터: {my_stack.pop()}") # C
print(f"추출된 데이터: {my_stack.pop()}") # B

# 5. 비어있는지 확인
print(f"스택이 비었나요?: {my_stack.isEmpty()}") # False