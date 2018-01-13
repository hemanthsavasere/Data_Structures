def binary_tree(root):
    return [root, [], []]


def insert_child_left(root, child):
    t = root.pop(1)
    if len(t) == 0:
        root.insert(1, [child, [], []])
    else:
        root.insert(1, [child, t, []])


def insert_child_right(root, child):
    t = root.pop(2)
    if len(t) == 0:
        root.insert(2, [child, [], []])
    else:
        root.insert(2, [child, [], t])


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


tree1 = binary_tree(3)
print tree1
insert_child_left(tree1, 4)
print tree1
insert_child_right(tree1, 5)
print tree1
insert_child_left(tree1, 6)
print tree1
insert_child_right(tree1, 8)
print tree1
print get_left_child(tree1[1])
