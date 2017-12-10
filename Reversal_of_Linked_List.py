from Linked_List import Node

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

temp = a
while temp is not None:
    print temp.value
    temp = temp.next

temp = a.next
head2 = Node(a.value)
prev = head2
while temp is not None:
    l = Node(temp.value)
    l.next = prev
    temp = temp.next
    prev = l

temp = l

while temp is not None:
    print "reverse value",temp.value
    temp = temp.next

prev = a
temp = a.next
nxt = None
a.next = None

while temp is not None:
    nxt = temp.next
    temp.next = prev
    prev = temp
    temp = nxt

temp = prev
print prev, prev.value

while temp is not None:
    print temp.value
    temp = temp.next

