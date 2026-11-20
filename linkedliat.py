# Create a link list and insert as specific position and 
#print the link 
#  delete a specific position and print the link list and 
# delete node from middle 

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,new_node):
        if self.head==None:
            temp=self.head
            return

        else:
            temp=self.head
            while True: 
                if new_node==None:
                    new_node=temp
                    temp=new
                    

