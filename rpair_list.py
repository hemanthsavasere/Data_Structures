class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(1)
node2 = Node(2)
node3 = Node(3)
head.next = node2
node2.next = node3
node3.next = head

arr = []
temp = head
prev = None
while temp is not None:
    if temp.next in arr:
        break
    else:
        print temp.value
        arr.append(temp.next)
        prev = temp
        temp = temp.next

print prev.value
prev.next = None

while temp is not None:
    print temp.value
    temp = temp.next
