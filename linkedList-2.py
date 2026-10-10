class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def _init_(self, head):
        self.head = head

    def insertNode(self, pos, value):
        new_node = Node(value)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head

            for i in range(pos - 2):
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head

        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next

    def findMiddle(self):
        slow = fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        print("\nMiddle node:", slow.data)

    def deleteNode(self, pos):
        if pos == 1:
            self.head = self.head.next
        else:
            temp = self.head

            for i in range(pos - 2):
                temp = temp.next

            temp.next = temp.next.next

    def reverseList(self):
        prev = None
        temp = self.head

        while temp != None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

    def pairSum(self):
        temp = self.head

        while temp != None and temp.next != None:
            total = temp.data + temp.next.data
            print(total, end=" ")
            temp = temp.next


a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.next = b
b.next = c
c.next = d

obj = LinkedList(a)

obj.insertNode(2, 15)
obj.display()

obj.findMiddle()

obj.deleteNode(4)
obj.display()

print()
# obj.reverseList()
# obj.display()

obj.pairSum()
