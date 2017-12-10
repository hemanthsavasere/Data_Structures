class Node(object):
    def __init__(self, val):
        self.value = val
        self.next = None

    def add_beginning(self,node):
        node.next = self


if __name__ == "__main__":
    head = Node(1)
    b = Node(2)
    head.next = b
    c = Node(5)
    b.next = c
    temp = head
    while temp is not None:
        print temp.value
        temp = temp.next
