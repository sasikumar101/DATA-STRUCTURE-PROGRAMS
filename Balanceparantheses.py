class BalanceOfParantheses:
    def __init__(self,size):
        self.stack=[]
        self.size=size
    def validexpression(self,expr):
        for char in expr:
            if char in '[{(':
                self.push(char)
            elif char in ']})':
                if not self.stack: # To check stack is empty
                    print("Right parantheses is more than left")
                    return False
                else:
                    temp=self.pop()
                    if not self.Match(temp,char):
                        print("Parantheses mismatched",temp,char)
                        return False
        if not self.stack:
            return  True
        else:
            print("Left parantheses is more than right")
            return False

    def push(self,char):
        if len(self.stack)==size:
            print("Over flow!")
        else:
            self.stack.append(char)
 
    def pop(self):
        if not self.stack:
            print("Under flow!")
        else:
            return self.stack.pop()

    def Match(self,temp,char):
        if temp =='{' and char=='}':
            return True
        if temp =='[ ' and char==']':
            return True
        if temp =='(' and char==')':
            return True
        return False


if __name__=="__main__":
    expr=input("Enter the expression:")
    size=int(input("Enter the size:"))
    a=BalanceOfParantheses(size)
    valid=a.validexpression(expr)
    if  valid:
        print ("balanced")
    else:
        print("UnBalanced")