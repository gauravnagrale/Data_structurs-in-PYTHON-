class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None
class Doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def createLL(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.next = None
        self.prev = None
        print('Doubly-Linked LIst is Created')

    def printLL(self):
        if self.head is None:
            print('Linked List is Empty')
            return
        else:
            itr = self.head
            llstr = ''
            while itr:
                llstr += str(itr.value)+'-->'
                itr = itr.next
            print(llstr)

    def insert(self, value, loc):
        newNode = Node(value)
        if self.head is None:
            print('The Linked_list is Empty')
            return
        else:
            if loc == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif loc == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                itr = self.head
                ind = 0
                while ind < loc-1:
                    itr = itr.next
                    ind += 1
                nextNode = itr.next
                newNode.prev = itr
                newNode.next = nextNode
                nextNode.prev = newNode
                itr.next = newNode
    def delete(self,loc):
        if self.head is None:
            print('The Linked-List is Empty')
            return
        else:
            if loc == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif loc == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                temp = self.head
                ind = 0
                while ind < loc-1:
                    temp = temp.next
                    ind += 1
                temp.next = temp.next.next
                temp.next.prev = temp
    def DeleteALl(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None
        print('The Doubly-Linked-List is Destroyed')
    def search(self,ele):
        temp = self.head
        while temp is not None:
            if temp.value == ele:
                print('Found the ELEMENT:',temp.value)
                break
            temp = temp.next
        else:
            print('The element is not present in the Linked-List')

    def reverse_traverse(self):
        temp = self.tail
        while temp:
            print(temp.value, end='-->')
            temp = temp.prev

DLL = Doubly_linked_list()
DLL.createLL(0)
DLL.printLL()
DLL.insert(10, 0)
DLL.insert(11, 0)
DLL.insert(12, 0)
DLL.insert(13, 0)
DLL.insert(100, 2)
DLL.insert(200,3)
DLL.printLL()
print('traversing from back')
DLL.reverse_traverse()
DLL.delete(1)
print('After deleting the element')
DLL.printLL()
DLL.search(200)
print('Deleting the LL')
DLL.DeleteALl()
