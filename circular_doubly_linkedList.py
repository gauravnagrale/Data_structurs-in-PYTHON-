class Node:
    def __init__(self,value = None):
        self.value  =value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        if self.head is None:
            print('Linked List is Empty')
        else:
            itr = self.head
            llstr = ''
            while itr:
                llstr += str(itr.value)+'-->'
                itr = itr.next
                if itr == self.tail.next:
                    break
            print(llstr)

    def create(self, value):
        newNode = Node(value)
        self.head = newNode# here the head is pointing to the new node
        self.tail = newNode# tail is also pointing to the new Node
        self.next = newNode# as it is a circular linked list it is pointing it the same node
        self.prev = newNode# and as it is a doubly linked list then prev node is pointing to the newly created node
        print('Circular Doubly Linked-List is created successfully')

    def insert(self,value,loc):
        if self.head is None:
            print('Linked-List is empty')
        else:
            newNode = Node(value)
            if loc == 0:
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.tail.next = newNode
                self.head = newNode
            elif loc == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                itr = self.head
                ind = 0
                while ind < loc-1:
                    itr = itr.next
                    ind += 1
                nextNode = itr.next
                newNode.next = itr.next
                newNode.prev = itr
                #newNode.next.prev = newNode
                nextNode.prev = newNode
                itr.next = newNode
    def delete(self,loc):
        if self.head is None:
            print('The linked_list is empty')
        else:
            if loc == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head

    def search_ele(self,ele):
        temp = self.head
        while temp:
            if temp.value is ele:
                print('Found the element',temp.value)
                break
            temp = temp.next
        else:
            print("Element is not present in the linked_list")

    def rev_traverse(self):
        if self.head is None:
            print('The Linked-List Empty')
        else:
            temp = self.tail
            while temp:
                print(temp.value, end='-->')
                temp = temp.prev
                if temp == self.tail:
                    break

CDLL = CircularDoublyLinkedList()
CDLL.create(10)
CDLL.insert(11, 0)
CDLL.insert(12, 1)
CDLL.insert(13, 1)
CDLL.insert(100, 2)
CDLL.print()
print('printing the reverse CDoubly Linked List')
CDLL.rev_traverse()
print()
CDLL.search_ele(100)
print('I am making changes to see if its get updated into the GitHun rep')