class Node:
  def __init__(self,val):
    self.data = val
    self.next = None
class LQueue:
  def __init__(self):
    self.front=self.rear=None
  def enqueue(self,new_node):
    if self.rear:
      self.rear.next = new_node
      self.rear = new_node
    else:
      self.front = self.rear = new_node
  def print(self):
    temp = self.front
    while temp:
      print(temp.data)
      temp = temp.next
  def dequeue(self):
    temp = self.front
    print("deleted node: ", temp.data)
    self.front = self.front.next
    # if self.
    temp = None
    if self.front:
      self.rear = None
      print("queue is empty")
      # self.front = self.front.next
que = LQueue()
que.enqueue(Node(23))
que.enqueue(Node(63))
que.enqueue(Node(78))
que.enqueue(Node(20))
que.print()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.print()
