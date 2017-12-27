class Node(object):
    def __init__(self, val):
        self.value = val
        self.next = None

    def add_beginning(self,node):
        node.next = self


if __name__ == "__main__":
    head = Node(1)
    b = Node(2)
    c = Node(5)
    head.next = b
    b.next = c
    temp = head
    while temp is not None:
        print temp.value
        temp = temp.next
