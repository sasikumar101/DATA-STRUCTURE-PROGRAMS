class Queue:
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = [0] * self.size
    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Overflow!")
        elif self.front == -1 and self.rear == -1:  
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print("Underflow!")
        elif self.front == self.rear:  # Only one elementn is left
            print("Deleted element:", self.queue[self.front])
            self.front = self.rear = -1
        else:
            print("Deleted element:", self.queue[self.front])
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue is empty!")
        i=self.front
        while (i!=self.rear):
            print(self.queue[i] ,end="->")
            i=(i+1)%self.size
        print(self.queue[i],"None")
    def peek(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            print("Front element:", self.queue[self.front])

size = int(input("Enter the queue size: "))
a = Queue(size)
for i in range(1, size + 1):
    data = int(input("Enter data element: "))
    a.enqueue(data)
a.display()
a.dequeue()
a.display()
