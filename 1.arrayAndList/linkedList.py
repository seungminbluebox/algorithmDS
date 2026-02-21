class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def addToHead(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode

    def addToPo(self, data,possition):
        if possition==0:
            self.addToHead(data)
            return
        newNode=Node(data)
        current=self.head
        for i in range(possition-1):
            if current is None:
                return
            current=current.next
        newNode.next=current.next
        current.next=newNode

    def delete(self, key):
        current=self.head
        prev=None
        while current:
            if current.data==key:
                if prev:
                    prev.next=current.next
                else:
                    self.head=current.next
                return
            prev=current    
            current=current.next

    def search(self,key):
        current=self.head
        while current:
            if current.data==key:
                return True
            current=current.next
        return False
    
    def traverse(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

s=LinkedList()
s.addToHead(10)
s.addToHead(30)
s.addToPo(20,1)
s.search(20)
s.delete(30)
s.traverse()

