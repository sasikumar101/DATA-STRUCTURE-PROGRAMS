class Node:
    def __init__(self,coeff,expo):
       self.coeff=coeff
       self.expo=expo
       self.next=None
class POLY:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,coeff,expo):
        num=int(input("Enter the no of polynomial node:"))
        for i in range(num):
            coeff=int(input("Enter the coefficient value of node:"))
            expo=int(input("Enter the exponent value of node:"))
            newnode=Node(coeff,expo)
            if self.head is None or newnode.expo>self.head.expo:
                newnode.next=self.head
                self.head=newnode
            else:
                self.temp=self.head
                while self.temp.next is not None and newnode.expo<self.temp.next.expo:
                    self.temp=self.temp.next
                newnode.next=self.temp.next
                self.temp.next=newnode
    def display(self):
        self.temp=self.head
        while self.temp is not None:
            print(f"{self.temp.coeff}x^{self.temp.expo}" ,end ="+")
            self.temp=self.temp.next
        print("None")
    


a=POLY()
a.create()
a.display()
   
              