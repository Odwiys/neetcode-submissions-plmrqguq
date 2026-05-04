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
        cur = head
        linker = {None : None}
        while cur:
            copy = Node(cur.val)
            linker[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = linker[cur]
            copy.next = linker[cur.next]
            copy.random = linker[cur.random]
            cur = cur.next

        return linker[head]