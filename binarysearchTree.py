class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None: #creating the root node
            self.root = new_node
            return

        else:
            temp = self.root #create new node for comparison

            while True:
                #compare new_node data to temp node data for left subtree
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left

                #compare new_node data to temp node data for right subtree
                elif new_node.data > temp.data:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

                else:
                    return

    def inorder(self, node): #recursive function to traverse the tree in inorder
        if node is None:
            return
        else:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)


btree = BST()

btree.insert(Node(10))
btree.insert(Node(5))
btree.insert(Node(15))
btree.insert(Node(45))
btree.insert(Node(25))

btree.inorder(btree.root)