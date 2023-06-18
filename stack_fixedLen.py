class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False

    def push(self,value):
        if self.isFull():
            print("Stack is FUll")
        else:
            self.list.append(value)
            return "Element has been inserted"

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            self.list.pop()

    #here we are going to see only the top element
    def peek(self):
        if self.isEmpty():
            return "The Linked-List is Empty"
        else:
            return self.list[len(self.list)-1]

fixedStack = Stack(5)
fixedStack.push(0)
fixedStack.push(1)
fixedStack.push(2)
fixedStack.push(3)
fixedStack.push(4)
print(fixedStack)
#fixedStack.push(0)
print(fixedStack.peek())


