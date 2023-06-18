class Stack:
    def __init__(self, maxsize):
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

    #push using append method
    def push(self,value):
        self.list.append(value)
        return "the Stack is Updated"

    #pop using the inbuilt method
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            self.list.pop()
            print("Element is removed")

    def delete(self):
        self.list = None
        print("We have successfully deleted the complete Stack")


CustStack = Stack()
print(CustStack.isEmpty())
CustStack.push(10)
CustStack.push(11)
CustStack.push(12)
print(CustStack)
CustStack.pop()
print(CustStack)
CustStack.delete()
CustStack.isEmpty()