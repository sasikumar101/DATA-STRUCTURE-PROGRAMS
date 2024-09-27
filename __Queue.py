class Queue:
    def __init__(self,size):
        self.size=size
        self.front=-1
        self.rear=-1
        self.queue=[0]*self.size
    def enqueue(self,data):
        if (self.rear==self.size-1):
            print("Over flow!")
        elif(self.front ==-1 and self.rear==-1):
            self.front=0 
            self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear=self.rear+1
            self.queue[self.rear]=data
    def dequeue(self):
        if (self.front==-1 and self.rear==-1):
            print("Under flow!")
        elif(self.front==self.rear):
            print("Delete element",self.queue[self.front])
            self.front=self.rear=-1
        else:
            print("Delete the first element!:",self.queue[self.front])
            self.front=self.front+1
    def display(self):
        print("The Queue elements:")
        for i in range(self.front,self.rear+1):
            print(self.queue[i],end="->")
        print("None")
    def peek(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is empty!")
        else:
            print("\nThe front elements:",self.queue[self.front])
size=int(input("Enter the queue size:"))
a=Queue(size)
for i in range(1,size+1):
    data=int(input("Enter the data elements:"))
    a.enqueue(data)
a.display()
a.dequeue()
a.peek()
