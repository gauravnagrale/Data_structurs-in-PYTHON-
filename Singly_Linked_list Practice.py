# linked List practice
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        if self.head == None:
            print('Linked-List is Empty')
            return
        else:
            temp = self.head
            llstr = ''
            while temp:
                llstr += str(temp.value)+'-->'
                temp = temp.next
            print(llstr)

    def insert(self,value,loc):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if loc == 0:
                newNode.next = self.head
                self.head = newNode
            elif loc == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                temp = self.head
                ind = 0
                while ind < loc-1:
                    temp = temp.next
                    ind += 1
                nextNode = temp.next
                temp.next = newNode
                newNode.next = nextNode
    def search(self,ele):
        temp = self.head
        count = 1

        while temp:
            if temp.value is ele:
                print('You have found the value at position:',count)
                return
            count += 1
            temp = temp.next
    def delete(self,loc):
        if self.head is None:
            print('Singly-Linked-List is EMPTY!')
        else:
            if loc == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif loc == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    temp = self.head
                    while temp:
                        if temp.next == self.tail:
                            break
                        temp = temp.next
                    temp.next = None
                    self.tail = temp
            else:
                temp = self.head
                ind = 1

                while ind < loc-1:
                    temp = temp.next
                    ind += 1
                new = temp.next
                temp.next = new.next

#main Function
SLL = SLinkedList()
SLL.insert(0, 0)
SLL.insert(1, 0)
SLL.insert(2, 0)
SLL.insert(3, 0)
SLL.insert(4, 1)
SLL.insert(10, 3)
SLL.print()
SLL.search(10)
SLL.delete(0)
SLL.print()
