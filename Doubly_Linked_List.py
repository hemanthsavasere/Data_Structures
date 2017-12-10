class Node(object):
    def __init__(self, val):
        self.value = val
        self.front = None
        self.back = None


a = Node(1)
b = Node(2)
c = Node(3)

a.front = b
b.front = c
b.back = a
c.back = b

temp = a

while temp.front is not None:
    print temp.value
    temp = temp.front

d = Node(4)
temp.front = d
d.back = temp

head = Node(0)
head.front = a
a.back = head

temp = head
cnt = 0

# while temp is not None:
#     print "the value for node", cnt+1, "is ", temp.value
#     temp = temp.front
#     cnt += 1

key = 3
temp1 = head
temp2 = Node(-2)

while temp1 is not None and key != temp1.value:
    print temp1.value
    temp2 = temp1
    temp1 = temp1.front

print "temps is now at ", temp1.value, temp2.value

f = Node(7)
temp2.front = f
f.back = temp2
f.front = temp1
temp1.back = f

temp = head
while temp is not None:
    print temp.value
    temp = temp.front

temp1 = head
while temp1 is not None and key != temp1.value:
    print temp1.value
    temp1 = temp1.front
    temp2 = temp1.front

print "temps is now at ", temp1.value, temp2.value

k = Node(8)
k.front = temp2
temp2.back = k
k.back = temp1
temp1.front = k

temp = head

while temp is not None:
    print temp.value
    temp = temp.front
