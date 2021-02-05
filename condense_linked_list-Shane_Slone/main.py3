# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def condense_linked_list(node):
    seen = set()
    cur = node
    prev = None
    while cur is not None:
        next_node = cur.next
        if cur.value in seen:
            prev.next = next_node
            cur.next = None
            cur = next_node
        else:
            seen.add(cur.value)
            prev = cur
            cur = next_node
    return node
            

