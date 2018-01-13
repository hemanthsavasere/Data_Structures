class binarytree(object):
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insert_left(self, leftchild):

        if self.left == None:
            t = binarytree(leftchild)
            self.left = t
        else:
            t = binarytree(leftchild)
            temp = self.left
            self.left = t
            t.left = temp

    def insert_right(self, rightchild):

        if self.right == None:
            t = binarytree(rightchild)
            self.right = t
        else:
            t = binarytree(rightchild)
            temp = self.right
            self.right = t
            t.right = temp

    def get_root(self):
        return self.key

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right


tree1 = binarytree(1)
tree1.insert_left(2)
tree1.insert_right(3)
tree1.insert_left(4)
tree1.insert_right(5)

def preorder_traversal(tree):
    if tree == None:
        return 0
    else:
        print tree.key
        preorder_traversal(tree.left)
        preorder_traversal(tree.right)


def preorder_traversal(tree):
    if tree == None:
        return 0
    else:
        print tree.key
        preorder_traversal(tree.left)
        preorder_traversal(tree.right)


def inorder_traversal(tree):
    if tree == None:
        return 0
    else:
        inorder_traversal(tree.left)
        print tree.key
        inorder_traversal(tree.right)


def postorder_traversal(tree):
    if tree == None:
        return 0
    else:
        postorder_traversal(tree.left)
        postorder_traversal(tree.right)
        print tree.key


print "pre-order"
preorder_traversal(tree1)
print
print

print "in-order"
inorder_traversal(tree1)
print
print

print "post-order"
inorder_traversal(tree1)
