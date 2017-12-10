import Linked_List


def cycle_check(a):
    temp = a.next
    while temp is not None:
        print temp.value, a.value
        if temp == a:
            return True
        else:
            temp = temp.next

    return False


a = Linked_List.Node(1)
b = Linked_List.Node(2)
c = Linked_List.Node(3)

a.next = b
b.next = c
c.next = a

print cycle_check(a)