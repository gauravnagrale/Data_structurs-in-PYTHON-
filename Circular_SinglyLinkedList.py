class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class ClinkedList:
    def __int__(self):
        self.head = None
        self.tail = None 

    def printLL(self):
        if self.head is None:
            print('Linked-List is empty')
        else:
            itr = self.head
            llst=''
            #iterating through the LL till we get the NULL value
            while itr:
                llst += str(itr.value)+'-->'
                itr=itr.next
                if itr == self.tail.next:
                    break
            print(llst)
    def create(self,value):
        new = Node(value)
        new.next = new # here the Node is poiniting to itself
        self.head = new
        self.tail = new

    def insert(self, value, loc):
        newNode = Node(value)
        if self.head == None:
            print('Circular-Linked List is Empty')
            return
        else:
            if loc == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode

            elif loc == 1:
                newNode.next = self.head
                self.tail = newNode
                self.tail.next = newNode

            else:
                temp = self.head
                ind = 0
                while ind < loc-1:
                    temp = temp.next
                    ind += 1
                a = temp.next
                temp.next = newNode
                newNode.next = a

    def delete(self, loc):
        if self.head is None:
            print('The Linked-List is EMPTY')
        else:
            if loc == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif loc == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    temp = self.head
                    while temp:
                        if temp.next == self.tail:
                            break
                        temp = temp.next
                    a = temp.next
                    temp.next = a.next
            else:
                temp = self.head
                ind = 0
                while ind < loc:
                    temp = temp.next
                    ind += 1
                a = temp.next
                temp.next = a.next

CLL = ClinkedList()
CLL.create(0)

CLL.insert(1, 0)
CLL.insert(2, 0)
CLL.insert(3, 0)
CLL.insert(4, 0)
CLL.insert(5, 1)
CLL.printLL()