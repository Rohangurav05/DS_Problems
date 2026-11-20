class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(10)
n1.next = Node(20)
n1.next.next = Node(30)

def display(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

def insert(head, data, pos):
    new = Node(data)
    if pos == 0:
        new.next = head
        return new
    temp = head
    for _ in range(pos - 1):
        temp = temp.next
    new.next = temp.next
    temp.next = new
    return head

def delete(head, value):
    if head and head.data == value:
        return head.next
    temp = head
    while temp and temp.next:
        if temp.next.data == value:
            temp.next = temp.next.next
            break
        temp = temp.next
    return head

def reverse(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

print("Original list:")
display(n1)

print("Middle node:", middle(n1))

print("Consecutive sums:")
temp = n1
while temp and temp.next:
    print(temp.data + temp.next.data)
    temp = temp.next

n1 = insert(n1, 15, 1)
print("After insertion:")
display(n1)

n1 = delete(n1, 20)
print("After deletion:")
display(n1)

n1 = reverse(n1)
print("After reversing:")
display(n1)
