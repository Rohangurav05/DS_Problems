# BST using Linked List

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.leftcnt=0

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node

        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left

                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def delete_node(self, rt, val):
        if rt is None:
            return None

        if val < rt.data:
            rt.left = self.delete_node(rt.left, val)

        elif val > rt.data:
            rt.right = self.delete_node(rt.right, val)

        else:
            if rt.left is None:
                return rt.right

            elif rt.right is None:
                return rt.left

            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.delete_node(rt.right, succ.data)

        return rt


    def get_successor(self, rt):
        temp = rt.right

        while temp.left is not None:
            temp = temp.left

        return temp
    
    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            if rt.left is None and rt.right is None:
                self.leftcnt+=1
            self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    def count_nodes(self, rt):
        if rt is None:
            return 0

        return 1 + self.count_nodes(rt.left) + self.count_nodes(rt.right)

    def findminmax(self):
        if self.root is None:
            print("BST is empty")
            return

        temp = self.root

        while temp.left:
            temp = temp.left

        print("\nMin:", temp.data)

        temp = self.root

        while temp.right:
            temp = temp.right

        print("Max:", temp.data)


# Main program

b1 = BST()

b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))

# print("\nInorder:")
# b1.inorder(b1.root)

# print("\nNo of nodes:", b1.count_nodes(b1.root))

# print("\nNo leafs nodes:", b1.leftcnt)
# print("\nPreorder:")
# b1.preorder(b1.root)

# print("\nPostorder:")
# b1.postorder(b1.root)

#b1.findminmax()

b1.delete_node(b1.root,10)
print("After Deletion : ",end="")
b1.inorder(b1.root)

# BST using Linked List

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.leftcnt = 0

    # Insert node
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node

        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left

                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    # Delete node
    def delete_node(self, rt, val):
        if rt is None:
            return None

        if val < rt.data:
            rt.left = self.delete_node(rt.left, val)

        elif val > rt.data:
            rt.right = self.delete_node(rt.right, val)

        else:
            # Node with no left child
            if rt.left is None:
                return rt.right

            # Node with no right child
            elif rt.right is None:
                return rt.left

            # Node with both left and right children
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.delete_node(rt.right, succ.data)

        return rt

    # Find inorder successor
    def get_successor(self, rt):
        temp = rt.right

        while temp.left is not None:
            temp = temp.left

        return temp

    # Inorder traversal
    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")

            if rt.left is None and rt.right is None:
                self.leftcnt += 1

            self.inorder(rt.right)

    # Preorder traversal
    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    # Postorder traversal
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    # Count total nodes
    def count_nodes(self, rt):
        if rt is None:
            return 0

        return 1 + self.count_nodes(rt.left) + self.count_nodes(rt.right)

    # Find minimum and maximum
    def findminmax(self):
        if self.root is None:
            print("BST is empty")
            return

        temp = self.root

        while temp.left:
            temp = temp.left

        print("\nMin:", temp.data)

        temp = self.root

        while temp.right:
            temp = temp.right

        print("Max:", temp.data)


# Main program

b1 = BST()

b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))

print("\nInorder:")
b1.inorder(b1.root)

print("\n\nPreorder:")
b1.preorder(b1.root)

print("\n\nPostorder:")
b1.postorder(b1.root)

print("\n\nTotal nodes:", b1.count_nodes(b1.root))

b1.leftcnt = 0
b1.inorder(b1.root)
print("\nLeaf nodes:", b1.leftcnt)

b1.findminmax()

# Delete node
b1.root = b1.delete_node(b1.root, 10)

print("\n\nAfter Deletion:")
b1.inorder(b1.root)

print("\n\nTotal nodes after deletion:", b1.count_nodes(b1.root))
