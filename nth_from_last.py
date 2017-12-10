# coding: utf-8

# # Linked List Nth to Last Node
#
# ## Problem Statement
# Write a function that takes a head node and an integer value **n** and then returns the nth to last node in the linked list. For example, given:

# In[87]:


def nth_to_last_node(n, head):
    temp = head
    prev = None
    cnt = 0
    while temp is not None:
        prev = temp
        temp = temp.nextnode
        cnt += 1

    cnt2 = 0
    traverse = cnt - (n)
    temp = head

    while cnt2 < traverse:
        cnt2 += 1
        temp = temp.nextnode

    return temp


class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode = None


# **Example Input and Output:**

# In[83]:


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a)

# In[84]:


# ## Solution
# Fill out your solution below:

# In[86]:


# # Test Your Solution

# In[88]:


"""
RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE 

PLEASE NOTE THIS IS JUST ONE CASE
"""

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e


####

class TestNLast(object):

    def test(self, sol):
        assert_equal(sol(2, a), d)
        print 'ALL TEST CASES PASSED'


# Run tests
t = TestNLast()
t.test(nth_to_last_node)

# ## Good Job!
