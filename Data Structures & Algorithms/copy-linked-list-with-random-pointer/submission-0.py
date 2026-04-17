"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # set hashmap that holds {og node: copy node (just the val)}
        og_to_copy = {}

        # first pass -> assigning key > og node and value > copy node but just the value
        curr = head
        while curr:
            og_to_copy[curr] = Node(curr.val)
            curr = curr.next

        # second pass -> assigning copy to the next and random pointers
        curr = head
        while curr:
            og_to_copy[curr].next = og_to_copy.get(curr.next)
            og_to_copy[curr].random = og_to_copy.get(curr.random)
            curr = curr.next

        # return the copy of the head
        return og_to_copy[head]